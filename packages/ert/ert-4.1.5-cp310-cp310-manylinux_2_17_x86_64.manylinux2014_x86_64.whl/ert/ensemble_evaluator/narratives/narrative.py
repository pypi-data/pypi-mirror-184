import asyncio
import base64
import json
import threading
import uuid
from asyncio.events import AbstractEventLoop
from asyncio.queues import QueueEmpty
from enum import Enum
from http import HTTPStatus
from typing import Any, Callable, Dict, List, Optional, Tuple, TypedDict, Union

from cloudevents.conversion import to_json
from cloudevents.http import CloudEvent, from_json
from cloudevents.sdk import types
from websockets.client import connect
from websockets.server import WebSocketServer  # type: ignore
from websockets.server import serve

from ert.async_utils import get_event_loop

from .._wait_for_evaluator import wait_for_evaluator

_DATACONTENTTYPE = "datacontenttype"

# An empty/missing datacontenttype is equivalent to json, so make it default.
# See https://github.com/cloudevents/spec/blob/v1.0.1/spec.md#datacontenttype
_DEFAULT_DATACONTETYPE = "application/json"


class _CloudEventSerializer:
    def __init__(self) -> None:
        self._marshallers: Dict[str, types.MarshallerType] = {}
        self._unmarshallers: Dict[str, types.UnmarshallerType] = {}

    def register_marshaller(
        self, datacontenttype: str, marshaller: types.MarshallerType
    ) -> "_CloudEventSerializer":
        self._marshallers[datacontenttype] = marshaller
        return self

    def register_unmarshaller(
        self, datacontenttype: str, unmarshaller: types.UnmarshallerType
    ) -> "_CloudEventSerializer":
        self._unmarshallers[datacontenttype] = unmarshaller
        return self

    def to_json(
        self, event: CloudEvent, data_marshaller: types.MarshallerType = None
    ) -> Union[str, bytes]:
        if not data_marshaller:
            datacontenttype = (
                event[_DATACONTENTTYPE]
                if _DATACONTENTTYPE in event
                else _DEFAULT_DATACONTETYPE
            )
            data_marshaller = self._marshallers.get(datacontenttype)
        return to_json(event, data_marshaller=data_marshaller)

    def from_json(
        self,
        data: Union[str, bytes],
        data_unmarshaller: types.UnmarshallerType = None,
    ) -> CloudEvent:
        raw_ce = json.loads(data)
        if not data_unmarshaller:
            datacontenttype = (
                raw_ce[_DATACONTENTTYPE]
                if _DATACONTENTTYPE in raw_ce
                else _DEFAULT_DATACONTETYPE
            )
            data_unmarshaller = self._unmarshallers.get(datacontenttype)
        return from_json(data, data_unmarshaller=data_unmarshaller)


class _ConnectionInformation(TypedDict):  # type: ignore
    uri: str
    proto: str
    hostname: str
    port: int
    path: str
    base_uri: str

    @classmethod
    def from_uri(cls, uri: str):
        proto, hostname, port = uri.split(":")
        path = ""
        if "/" in port:
            port, path = port.split("/")
        hostname = hostname[2:]
        path = "/" + path
        port = int(port)
        base_uri = f"{proto}://{hostname}:{port}"
        return cls(
            uri=uri,
            proto=proto,
            hostname=hostname,
            port=port,
            path=path,
            base_uri=base_uri,
        )


class ReMatch:
    # TODO: make regex a re.Pattern after migrating away from 3.6.
    # See https://github.com/equinor/ert/issues/1702
    def __init__(self, regex: Any, replace_with: str) -> None:
        self.regex = regex
        self.replace_with = replace_with


class EventDescription(TypedDict):  # type: ignore
    id_: str
    source: Union[str, ReMatch]
    type_: Union[str, ReMatch]
    datacontenttype: Optional[Union[str, ReMatch]]
    subject: Optional[Union[str, ReMatch]]
    data: Optional[Any]


class _Event:
    def __init__(self, description: EventDescription) -> None:
        self._original_event_description = description
        self._id = description.get("id_", uuid.uuid4())
        self.source = description["source"]
        self.type_ = description["type_"]
        self.datacontenttype = description.get(_DATACONTENTTYPE)
        self.subject = description.get("subject")
        self.data = description.get("data")

    def __repr__(self) -> str:
        s = "Event("
        for attr in [
            (self.source, "Source"),
            (self.type_, "Type"),
            (self.datacontenttype, "DataContentType"),
            (self.subject, "Subject"),
            (self.data, "Data"),
        ]:
            if isinstance(attr[0], ReMatch):
                s += f"{attr[1]}: {attr[0].regex} "
            elif attr[0]:
                s += f"{attr[1]}: {attr[0]} "
        s += f"Id: {self._id})"
        return s

    def dict_match(self, original, match, msg_start, path=""):
        assert isinstance(original, dict), f"{msg_start}data is not a dict"
        for k, v in match.items():
            kpath = f"{path}/{k}"
            assert isinstance(original, dict)
            assert k in original, f"{msg_start}{kpath} not present in data"
            if isinstance(v, dict):
                assert isinstance(original[k], dict), f"{msg_start}{kpath} not a dict"
                self.dict_match(original[k], v, msg_start, kpath)
            elif isinstance(v, ReMatch):
                assert isinstance(original[k], str), f"{msg_start}{kpath} not a str"
                assert v.regex.match(
                    original[k]
                ), f"{msg_start}{kpath} did not match {v}"
            else:
                assert (
                    original[k] == v
                ), f"{msg_start}{kpath} value ({original[k]}) is not equal to ({v})"

    def assert_matches(self, other: CloudEvent):
        msg_tmpl = "{self} did not match {other}: {reason}"

        if isinstance(self.data, dict):
            self.dict_match(other.data, self.data, f"{self} did not match {other}: ")
        elif isinstance(self.data, bytes):
            assert self.data == other.data, msg_tmpl.format(
                self=self, other=other, reason=f"{self.data} != {other.data}"
            )

        for attr in filter(
            lambda x: x[0] is not None,
            [
                (self.source, "source"),
                (self.type_, "type"),
                (self.subject, "subject"),
                (self.datacontenttype, _DATACONTENTTYPE),
            ],
        ):
            if isinstance(attr[0], ReMatch):
                assert attr[0].regex.match(other[attr[1]]), msg_tmpl.format(
                    self=self,
                    other=other,
                    reason=f"no match for {attr[0]} in {attr[1]}",
                )
            else:
                assert attr[0] == other[attr[1]], msg_tmpl.format(
                    self=self, other=other, reason=f"{attr[0]} != {other[attr[1]]}"
                )

    def to_cloudevent(self) -> CloudEvent:
        attrs = {}
        for attr in [
            (self.source, "source"),
            (self.type_, "type"),
            (self.subject, "subject"),
            (self.datacontenttype, _DATACONTENTTYPE),
        ]:
            if isinstance(attr[0], ReMatch):
                attrs[attr[1]] = attr[0].replace_with
            else:
                attrs[attr[1]] = attr[0]
        data = {}
        if isinstance(self.data, dict):
            for k, v in self.data.items():
                if isinstance(v, ReMatch):
                    data[k] = v.replace_with
                else:
                    data[k] = v
        elif isinstance(self.data, bytes):
            data = self.data
        return CloudEvent(attrs, data)

    def _serialize(self, d: dict) -> dict:
        ret = {}
        for k, v in d.items():
            if isinstance(v, ReMatch):
                v = v.regex.pattern
            if isinstance(k, ReMatch):
                k = k.regex.pattern
            if isinstance(v, dict):
                v = self._serialize(v)
            elif isinstance(v, bytes):
                v = base64.b64encode(v).decode()
            ret[k] = v
        return ret

    def json(self) -> dict:
        return self._serialize(self._original_event_description)


class InteractionDirection(Enum):
    RESPONSE = 1
    REQUEST = 2

    def represents(self, interaction):
        return (
            isinstance(interaction, (_Request, _RecurringRequest))
            and self == InteractionDirection.REQUEST
            or isinstance(interaction, (_Response, _RecurringResponse))
            and self == InteractionDirection.RESPONSE
        )


class _Interaction:
    def __init__(
        self,
        provider_states: Optional[List[Dict[str, Any]]],
        ce_serializer: _CloudEventSerializer,
    ) -> None:
        self.provider_states: Optional[List[Dict[str, Any]]] = provider_states
        self.scenario: str = ""
        self.events: List[_Event] = []
        self.direction = None
        self.ce_serializer = ce_serializer

    def json(self) -> dict:
        ret = {
            "provider_states": list(self.provider_states),
            "type": self.__class__.__name__[1:].lower(),
            "events": [event.json() for event in self.events],
        }
        if hasattr(self, "terminator"):
            ret["terminator"] = self.getattr("terminator").json()

        if self.scenario:
            ret["scenario"] = self.scenario
        return ret

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Scenario: {self.scenario})"

    def assert_matches(self, other: CloudEvent, event: Optional[_Event] = None):
        if not event:
            raise ValueError("must match against specific event for interaction")
        event.assert_matches(other)

    async def verify(
        self, msg_producer: Callable[[], Tuple[InteractionDirection, str]]
    ):
        for event in self.events:
            source, msg = await msg_producer()
            assert source.represents(
                self
            ), f"Wrong direction {source} when expecting {self}\n Got: {msg} instead"
            self.assert_matches(self.ce_serializer.from_json(msg), event)

    def generate(self):
        for event in self.events:
            yield self.ce_serializer.to_json(event.to_cloudevent())


class _RecurringInteraction(_Interaction):
    def __init__(
        self,
        provider_states: Optional[List[Dict[str, Any]]],
        terminator: _Event,
        ce_serializer: _CloudEventSerializer,
    ) -> None:
        super().__init__(provider_states, ce_serializer)
        self.terminator = terminator

    def assert_matches(self, other: CloudEvent, event: Optional[_Event] = None):
        terminator_error = None
        if event:
            raise ValueError("cannot match against specific event")
        try:
            self.terminator.assert_matches(other)
        except AssertionError as e:
            terminator_error = e
            pass
        else:
            raise _InteractionTermination()

        for ev in self.events:
            try:
                ev.assert_matches(other)
            except AssertionError:
                continue
            else:
                return

        raise AssertionError(
            f"No event in {self}\n matched {other}.\n"
            f"Did not match terminator because: {terminator_error}"
        )

    async def verify(
        self, msg_producer: Callable[[], Tuple[InteractionDirection, str]]
    ):
        while True:
            source, msg = await msg_producer()
            assert source.represents(
                self
            ), f"Wrong direction {source} when expecting {self}\n Got: {msg} instead"
            try:
                self.assert_matches(self.ce_serializer.from_json(msg))
            except _InteractionTermination:
                break

    def generate(self):
        for event in self.events:
            yield self.ce_serializer.to_json(event.to_cloudevent())
        yield self.ce_serializer.to_json(self.terminator.to_cloudevent())


class _Request(_Interaction):
    pass


class _RecurringRequest(_RecurringInteraction):
    pass


class _Response(_Interaction):
    pass


class _RecurringResponse(_RecurringInteraction):
    pass


class _InteractionTermination(Exception):
    pass


class _ProviderVerifier:
    def __init__(
        self,
        interactions: List[_Interaction],
        uri: str,
        ce_serializer: _CloudEventSerializer,
    ) -> None:
        self._interactions: List[_Interaction] = interactions
        self._uri = uri
        self._ce_serializer = ce_serializer

        # A queue on which errors will be put
        self._errors: asyncio.Queue = asyncio.Queue()
        self._ws_thread: Optional[threading.Thread] = None
        self._loop: Optional[asyncio.BaseEventLoop] = None

    def verify(self, on_connect):
        self._ws_thread = threading.Thread(
            target=self._sync_listener, args=[on_connect]
        )
        self._ws_thread.start()
        if get_event_loop().is_running():
            raise RuntimeError(
                "sync narrative should control the loop, "
                "maybe you called verify() from within an async test?"
            )
        self._ws_thread.join()
        errors = get_event_loop().run_until_complete(self._collect_errors())
        if errors:
            raise AssertionError(errors)

    async def _mock_listener(self, on_connect):
        async with connect(self._uri) as websocket:
            on_connect()
            await _mock_verify_handler(
                websocket.recv,
                websocket.send,
                self._interactions,
                self._errors,
                mock_direction=InteractionDirection.REQUEST,
                verify_direction=InteractionDirection.RESPONSE,
            )

    def _sync_listener(self, on_connect):
        self._loop = asyncio.new_event_loop()
        self._loop.run_until_complete(self._mock_listener(on_connect))
        self._loop.close()

    async def _collect_errors(self):
        errors: List[Exception] = []
        while True:
            try:
                errors.append(self._errors.get_nowait())
            except QueueEmpty:
                break
        return errors


async def _mock_verify_handler(
    receive_func, send_func, interactions, errors, mock_direction, verify_direction
):

    try:
        for interaction in interactions:
            if mock_direction.represents(interaction):
                for msg in interaction.generate():
                    await send_func(msg)
            elif verify_direction.represents(interaction):

                async def receive():
                    return verify_direction, await receive_func()

                await interaction.verify(receive)
            else:
                e = TypeError(
                    "the first interaction needs to be promoted "
                    "to either response or receive"
                )
                errors.put_nowait(e)
    except AssertionError as e:
        errors.put_nowait(e)
    except Exception as e:
        errors.put_nowait(e)
        raise


class _ProviderMock:
    def __init__(
        self,
        interactions: List[_Interaction],
        conn_info: _ConnectionInformation,
        ce_serializer: _CloudEventSerializer,
    ) -> None:
        self._interactions: List[_Interaction] = interactions
        self._loop: Optional[AbstractEventLoop] = None
        self._ws: Optional[WebSocketServer] = None
        self._conn_info = conn_info
        self._ce_serializer = ce_serializer
        self._done: Optional[asyncio.Future] = None

        # ensure there is an event loop in case we are not on main loop
        get_event_loop()
        # A queue on which errors will be put
        self._errors: asyncio.Queue = asyncio.Queue()

    @property
    def uri(self) -> str:
        return self._conn_info["uri"]

    @property
    def hostname(self) -> str:
        return self._conn_info["hostname"]

    @property
    def port(self) -> str:
        return self._conn_info["port"]

    async def _mock_handler(self, websocket, path):
        expected_path = self._conn_info["path"]
        if path != expected_path:
            print(f"not handling {path} as it is not the expected path {expected_path}")
            return
        await _mock_verify_handler(
            websocket.recv,
            websocket.send,
            self._interactions,
            self._errors,
            mock_direction=InteractionDirection.RESPONSE,
            verify_direction=InteractionDirection.REQUEST,
        )

    async def process_request(self, path, request_headers):
        if path == "/healthcheck":
            return HTTPStatus.OK, {}, b""

    def _sync_ws(self, delay_startup=0):
        self._loop = asyncio.new_event_loop()
        self._done = self._loop.create_future()

        async def _serve():
            await asyncio.sleep(delay_startup)
            ws = await serve(
                self._mock_handler,
                self._conn_info["hostname"],
                self._conn_info["port"],
                process_request=self.process_request,
            )
            await self._done
            ws.close()
            await ws.wait_closed()

        self._loop.run_until_complete(_serve())
        self._loop.close()

    async def _verify(self):
        errors = []
        while True:
            try:
                errors.append(self._errors.get_nowait())
            except QueueEmpty:
                break
        return errors

    def __enter__(self):
        self._ws_thread = threading.Thread(target=self._sync_ws)
        self._ws_thread.start()
        if get_event_loop().is_running():
            raise RuntimeError(
                "sync narrative should control the loop, "
                "maybe you called it from within an async test?"
            )
        get_event_loop().run_until_complete(
            wait_for_evaluator(self._conn_info["base_uri"])
        )
        return self

    def __exit__(self, *args, **kwargs):
        if self._loop and self._done:
            self._loop.call_soon_threadsafe(self._done.set_result, None)
        if self._ws:
            self._ws_thread.join()
        errors = get_event_loop().run_until_complete(self._verify())
        if errors:
            raise AssertionError(errors)

    async def __aenter__(self):
        self._ws = await serve(
            self._mock_handler, self._conn_info["hostname"], self._conn_info["port"]
        )
        return self

    async def __aexit__(self, *args):
        if self._ws:
            self._ws.close()
            await self._ws.wait_closed()
        errors = await self._verify()
        if errors:
            raise AssertionError(errors)


class _Narrative:
    def __init__(self, consumer: "Consumer", provider: "Provider") -> None:
        self.consumer = consumer
        self.provider = provider
        self.interactions: List[_Interaction] = []
        self.name: Optional[str] = None
        self._mock: Optional[_ProviderMock] = None
        self._conn_info: Optional[_ConnectionInformation] = None
        self._ce_serializer = _CloudEventSerializer()

    def given(self, provider_state: Optional[str], **params) -> "_Narrative":
        state = None
        if provider_state:
            state = [{"name": provider_state, "params": params}]
        self.interactions.append(_Interaction(state, self._ce_serializer))
        return self

    def and_given(self, provider_state: str, **params) -> "_Narrative":
        raise NotImplementedError("not yet implemented")

    def receives(self, scenario: str) -> "_Narrative":
        interaction = self.interactions[-1]
        # pylint: disable=unidiomatic-typecheck
        if type(interaction) == _Interaction:
            interaction.__class__ = _Request
        elif not interaction.events:
            raise ValueError("receive followed an empty response scenario")
        else:
            interaction = _Request(
                self.interactions[-1].provider_states, self._ce_serializer
            )
            self.interactions.append(interaction)
        interaction.scenario = scenario
        return self

    def responds_with(self, scenario: str) -> "_Narrative":
        interaction = self.interactions[-1]
        # pylint: disable=unidiomatic-typecheck
        if type(interaction) == _Interaction:
            interaction.__class__ = _Response
        elif (
            isinstance(interaction, (_Request, _RecurringRequest))
            and not interaction.events
        ):
            raise ValueError("response followed an empty request scenario")
        else:
            interaction = _Response(
                self.interactions[-1].provider_states, self._ce_serializer
            )
            self.interactions.append(interaction)
        interaction.scenario = scenario
        return self

    def cloudevents_in_order(self, events: List[EventDescription]) -> "_Narrative":
        cloudevents = []
        for event in events:
            cloudevents.append(_Event(event))
        self.interactions[-1].events = cloudevents
        return self

    def repeating_unordered_events(
        self, events: List[EventDescription], terminator=EventDescription
    ) -> "_Narrative":
        events_list = []
        for event in events:
            events_list.append(_Event(event))
        interaction = self.interactions[-1]
        # pylint: disable=unidiomatic-typecheck
        if type(interaction) == _Response:
            self.interactions[-1] = _RecurringResponse(
                interaction.provider_states, _Event(terminator), self._ce_serializer
            )
        elif isinstance(interaction, _Request):
            self.interactions[-1] = _RecurringRequest(
                interaction.provider_states, _Event(terminator), self._ce_serializer
            )
        elif isinstance(
            interaction, (_RecurringRequest, _RecurringResponse, _RecurringInteraction)
        ):
            raise TypeError(
                f"interaction {interaction} already recurring, define new interaction"
            )
        else:
            raise ValueError(f"cannot promote {interaction}")
        self.interactions[-1].events = events_list
        self.interactions[-1].scenario = interaction.scenario
        return self

    def on_uri(self, uri: str) -> "_Narrative":
        self._conn_info = _ConnectionInformation.from_uri(uri)
        return self

    def with_unmarshaller(
        self, datacontenttype: str, data_unmarshaller: types.UnmarshallerType
    ):
        self._ce_serializer.register_unmarshaller(datacontenttype, data_unmarshaller)
        return self

    def with_marshaller(
        self, datacontenttype: str, data_marshaller: types.MarshallerType
    ):
        self._ce_serializer.register_marshaller(datacontenttype, data_marshaller)
        return self

    @property
    def uri(self) -> str:
        if not self._conn_info:
            raise ValueError("no connection information")
        return self._conn_info.get("uri")

    def _reset(self):
        self._conn_info = None

    def __enter__(self):
        if not self._conn_info:
            raise ValueError("no connection info on mock")
        self._mock = _ProviderMock(
            self.interactions, self._conn_info, self._ce_serializer
        )
        return self._mock.__enter__()

    def __exit__(self, *args, **kwargs):
        self._mock.__exit__(*args, **kwargs)
        self._reset()

    async def __aenter__(self):
        if not self._conn_info:
            raise ValueError("no connection info on mock")
        self._mock = _ProviderMock(
            self.interactions, self._conn_info, self._ce_serializer
        )
        return await self._mock.__aenter__()

    async def __aexit__(self, *args):
        await self._mock.__aexit__(*args)
        self._reset()

    def verify(self, provider_uri, on_connect) -> _ProviderVerifier:
        _ProviderVerifier(self.interactions, provider_uri, self._ce_serializer).verify(
            on_connect
        )

    def json(self) -> dict:
        if not self.name:
            raise ValueError("narrative must have a name")
        ret = {
            "interactions": [interaction.json() for interaction in self.interactions],
            "name": self.name,
        }
        ret.update(self.provider.json())
        ret.update(self.consumer.json())
        return ret

    def with_name(self, name: str) -> "_Narrative":
        self.name = name
        return self


class _Actor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def json(self) -> dict:
        return {self.__class__.__name__.lower(): {"name": self.name}}


class Provider(_Actor):
    pass


class Consumer(_Actor):
    def forms_narrative_with(self, provider: Provider, **kwargs) -> _Narrative:
        return _Narrative(self, provider, **kwargs)
