import numpy as np
from typing import Any, Tuple, TYPE_CHECKING
from smartcapture.utils import getFromDict
from .logger import LOG_MESSAGES

if TYPE_CHECKING:
    from smartcapture.trigger import Trigger


class SCQLPredicate:
    def __init__(self, predicate: Any, autotags: dict, trigger: "Trigger"):
        self.predicate = predicate
        self.autotags = autotags
        self.trigger = trigger

    def evaluate(self, state: dict) -> Tuple[Any, int]:
        if type(self.predicate) != dict:
            return self.predicate, 0
        if len(self.predicate) == 1:
            key = list(self.predicate)[0]
            if key == "$and":
                return ANDExpression(
                    self.predicate["$and"], self.autotags, self.trigger
                ).evaluate(state)
            elif key == "$or":
                return ORExpression(
                    self.predicate["$or"], self.autotags, self.trigger
                ).evaluate(state)
            elif key == "$not":
                return not SCQLPredicate(
                    self.predicate["$not"], self.autotags, self.trigger
                ).evaluate(state)
            else:
                return ConditionOnField(
                    key, self.predicate[key], self.autotags, self.trigger
                ).evaluate(state)
        else:  # default to AND predicate mimicking MongoQL behavior
            and_predicate = [{k: v} for k, v in self.predicate.items()]
            return ANDExpression(and_predicate, self.autotags, self.trigger).evaluate(
                state
            )


class ANDExpression(SCQLPredicate):
    def evaluate(self, state: dict) -> bool:
        for condition in self.predicate:
            value, status_code = SCQLPredicate(
                condition, self.autotags, self.trigger
            ).evaluate(state)
            if status_code != 0:
                return False, status_code
            if value is False:
                return False, 0
        return True, 0


class ORExpression(SCQLPredicate):
    def evaluate(self, state: dict) -> bool:
        for condition in self.predicate:
            value, status_code = SCQLPredicate(
                condition, self.autotags, self.trigger
            ).evaluate(state)
            if status_code != 0:
                return False, status_code
            if value is True:
                return True, 0
        return False, 0


class ConditionOnField:
    def __init__(
        self, field: str, predicate: dict, autotags: dict, trigger: "Trigger"
    ) -> bool:
        self.field = field.split(".")
        self.predicate = predicate
        self.autotags = autotags
        self.trigger = trigger

    def evaluate(self, state):
        field_value = getFromDict(state, self.field)
        key = list(self.predicate)[0]
        if key == "$eq":
            return field_value == self.predicate[key], 0
        elif key == "$neq":
            return field_value != self.predicate[key], 0
        elif key == "$gt":
            return field_value > self.predicate[key], 0
        elif key == "$gte":
            return field_value >= self.predicate[key], 0
        elif key == "$lt":
            return field_value < self.predicate[key], 0
        elif key == "$lte":
            return field_value <= self.predicate[key], 0
        elif key == "$in":
            return field_value in self.predicate[key], 0
        elif key == "$autotag":
            autotag_id, threshold = self.predicate[key][0], self.predicate[key][1]
            autotag_coefficients = self.autotags[autotag_id]
            try:
                autotag_value = np.dot(field_value, autotag_coefficients)
                return bool(autotag_value >= threshold), 0
            except ValueError:
                self.trigger.logger.error(
                    LOG_MESSAGES["InvalidAutotagDims"],
                    extra={
                        "trigger_id": self.trigger.trigger_id,
                        "offending_field": ".".join(self.field),
                        "offending_value": str(self.predicate[key]),
                        "log_info": {"name": "InvalidAutotagDims"},
                    },
                )
                return False, 307
        else:
            self.trigger.logger.error(
                LOG_MESSAGES["InvalidSCQLSyntax"],
                extra={
                    "trigger_id": self.trigger.trigger_id,
                    "log_info": {"name": "InvalidSCQLSyntax"},
                },
            )
            return False, 202
