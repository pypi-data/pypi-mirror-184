import json
import time
from typing import Tuple
from .scql import SCQLPredicate
from .logger import Logger, LOG_MESSAGES


class Trigger:
    def __init__(
        self, trigger_id: str, predicate: str, metadata: dict, logger: Logger
    ) -> None:
        """
        Args:
        trigger_id: Unique identifier to identify triggers to be used
        predicate: Smart Capture Query predicate
        metadata: Additional data required to evaluate if a trigger should be activated.
        For example:
        {
            "autotags": {
                "tag_1": [0.5, 0.3, ...]
            },
            "sample_rate": 10,
        }

        """
        self.trigger_id = trigger_id
        self.autotags = metadata.get("autotags", {})
        self.sample_rate = metadata.get("sample_rate", 0)
        self.dataset_id = metadata.get("dataset_id", "")
        self.scql_version = metadata.get("scql_version", "1.0")
        self.predicate = SCQLPredicate(json.loads(predicate), self.autotags, self)
        self.last_activation = 0
        self.logger = logger

    def evaluate(self, state: dict) -> Tuple[bool, int]:
        """
        Evaluates if a trigger has been activated given the device state using the predicate

        Args:
        state: Dictionary containing state data of the device.

        Returns:
        Tuple containing:
        result: boolean indicating if the trigger has been activated.
        status_code: 0 if successful or error code if not.
        """
        if time.time() * 1000.0 < self.last_activation + self.sample_rate:
            return False, 1001
        try:
            result, status_code = self.predicate.evaluate(state)
        except KeyError as e:
            self.logger.error(
                LOG_MESSAGES["IncompleteTriggerState"],
                extra={
                    "trigger_id": self.trigger_id,
                    "offending_field": e.args[0],
                    "log_info": {"name": "IncompleteTriggerState"},
                },
            )
            return False, 302
        if result:
            self.last_activation = time.time() * 1000.0
        return result, status_code
