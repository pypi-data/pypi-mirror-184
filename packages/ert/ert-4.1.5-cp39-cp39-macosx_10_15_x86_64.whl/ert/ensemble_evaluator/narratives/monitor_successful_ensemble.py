import pickle
import re

import cloudpickle

from ert import serialization
from ert.ensemble_evaluator import identifiers, state

from .narrative import Consumer, EventDescription, Provider, ReMatch


def monitor_successful_ensemble():
    return (
        Consumer("Monitor")
        .forms_narrative_with(
            Provider("Ensemble Evaluator"),
        )
        .given("a successful one-member one-step one-job ensemble")
        .responds_with("starting snapshot")
        .cloudevents_in_order(
            [
                EventDescription(
                    type_=identifiers.EVTYPE_EE_SNAPSHOT,
                    source=ReMatch(
                        re.compile(r"/ert/ensemble/ee."), "/ert/ensemble/ee-0"
                    ),
                ),
            ]
        )
        .responds_with("a bunch of snapshot updates")
        .repeating_unordered_events(
            [
                EventDescription(
                    type_=identifiers.EVTYPE_EE_SNAPSHOT_UPDATE,
                    source=ReMatch(
                        re.compile(r"/ert/ensemble/ee."), "/ert/ensemble/ee-0"
                    ),
                ),
            ],
            terminator=EventDescription(
                type_=identifiers.EVTYPE_EE_SNAPSHOT_UPDATE,
                source=ReMatch(re.compile(r"/ert/ensemble/ee."), "/ert/ensemble/ee-0"),
                data={identifiers.STATUS: state.ENSEMBLE_STATE_STOPPED},
            ),
        )
        .receives("done")
        .cloudevents_in_order(
            [
                EventDescription(
                    type_=identifiers.EVTYPE_EE_USER_DONE,
                    source=ReMatch(re.compile(r"/ert/monitor/."), "/ert/monitor/007"),
                ),
            ]
        )
        .responds_with("termination")
        .cloudevents_in_order(
            [
                EventDescription(
                    type_=identifiers.EVTYPE_EE_TERMINATED,
                    source=ReMatch(
                        re.compile(r"/ert/ensemble/ee."), "/ert/ensemble/ee-0"
                    ),
                    datacontenttype="application/octet-stream",
                    data=cloudpickle.dumps("hello world"),
                ),
            ]
        )
        .with_marshaller("application/json", serialization.evaluator_marshaller)
        .with_unmarshaller("application/json", serialization.evaluator_unmarshaller)
        .with_unmarshaller("application/octet-stream", pickle.loads)
        .with_name("Monitor Successful Ensemble")
    )
