import base64
import json
import requests
from typing import List, Union, Tuple

from .trigger import Trigger
from .logger import Logger, LOG_MESSAGES
from .constants import SMARTCAPTURE_ENDPOINT


class SmartCaptureClient:
    def __init__(
        self,
        device_name: str,
        api_key: str = "",
        externally_hosted: bool = False,
        log_file: str = "sc_log.log",
    ) -> None:
        """
        Initializes the SmartCaptureClient.

        Args:
        device_name: Name of the device registered with SmartCapture.
        api_key: API key to be used to authenticate with the SmartCapture server.
        externally_hosted: If true, the client will not attempt to fetch device or trigger
            information from the SmartCapture server.
        log_file: Path of the log file to write to.

        Returns:
        status code: 0 if successful or error code if not.
        """
        if not api_key and not externally_hosted:
            raise Exception(
                "API key must be provided when using Scale SmartCapture Server"
            )
        self.logger = Logger("smartcapture_client", log_file)
        self.api_key = api_key
        self.encoded_key = base64.b64encode((self.api_key + ":").encode()).decode()
        self.device_name = device_name
        self.triggers = []
        if not externally_hosted:
            self.device_id = self._get_device_id()

    def _get_device_id(self) -> str:
        """
        Gets the device id from the SmartCapture server.

        Returns:
        device_id, status_code: Device id registered with SmartCapture and status code indicating
            success or failure.
        """
        resp = requests.get(
            f"{SMARTCAPTURE_ENDPOINT}/all_devices",
            headers={"Authorization": "Basic " + self.encoded_key},
        )
        for device in resp.json():
            if device["name"] == self.device_name:
                return device["id"]
        raise Exception("Device not registered on smart capture")

    def _deserialize_triggers(self, trigger_config: dict) -> List[Trigger]:
        """
        Deserializes the trigger configuration into a list of Trigger objects.

        Args:
        trigger_config: Trigger configuration JSON object to be deserialized.

        Returns:
        trigger_objects: List of Trigger objects.
        """
        last_activations = {
            trigger.trigger_id: trigger.last_activation for trigger in self.triggers
        }

        triggers = trigger_config.get("triggers", [])
        autotags = trigger_config.get("autotags", [])

        autotag_data = {}
        for autotag in autotags:
            id = autotag["id"]
            autotag_data[id] = autotag[id]

        trigger_objects = []
        for trigger in triggers:
            metadata = {
                "sample_rate": trigger["sample_rate"],
                "dataset_id": trigger["dataset_id"],
                "scql_version": trigger["scql_version"],
                "autotags": autotag_data,
            }

            trigger_object = Trigger(
                trigger["id"],
                json.dumps(trigger["predicate"]),
                metadata,
                self.logger,
            )
            if trigger["id"] in last_activations:
                trigger_object.last_activation = last_activations[trigger["id"]]

            trigger_objects.append(trigger_object)

        return trigger_objects

    def load(self, trigger_config: Union[str, dict]) -> int:
        """
        Loads triggers from json object or json file on device and prepares them for evaluation.

        Args:
        trigger_config: String containing path the json file with serialized trigggers or
            json object with serialized triggers.

        Returns:
        status code: 0 if successful or error code if not.
        """
        if type(trigger_config) == str:
            try:
                data = json.load(open(trigger_config))
            except FileNotFoundError:
                self.logger.error(
                    LOG_MESSAGES["PathNotFound"],
                    extra={"log_info": {"name": "PathNotFound"}},
                )
                return 101
            except PermissionError:
                self.logger.error(
                    LOG_MESSAGES["UnreadableFile"],
                    extra={"log_info": {"name": "UnreadableFile"}},
                )
                return 102
            except json.decoder.JSONDecodeError:
                self.logger.error(
                    LOG_MESSAGES["MalformedJSON"],
                    extra={"log_info": {"name": "MalformedJSON"}},
                )
                return 201
            self.triggers = self._deserialize_triggers(data)
        elif type(trigger_config) == dict:
            self.triggers = self._deserialize_triggers(trigger_config)
        else:
            self.logger.error(
                LOG_MESSAGES["InvalidType"],
                extra={"log_info": {"name": "InvalidType"}},
            )
            return 204

        self.logger.info(
            f"Loaded {len(self.triggers)} triggers.",
            extra={"log_info": {"name": "TriggersLoaded"}},
        )
        return 0

    def evaluate(self, state: dict) -> List[Tuple[str, bool, str, int]]:
        """
        Evaluates the triggers against the input state dictionary.

        Args:
        state: State to be evaluated against the triggers.

        Returns:
        List of tuples corresponding to triggers containing the trigger id, the result of the
            evaluation, the dataset id, and the status code.
        """
        trigger_results = []
        for trigger in self.triggers:
            result, status_code = trigger.evaluate(state)
            trigger_results.append(
                (trigger.trigger_id, result, trigger.dataset_id, status_code)
            )
        return trigger_results
