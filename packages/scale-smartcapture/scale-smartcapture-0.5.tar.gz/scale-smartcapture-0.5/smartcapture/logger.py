import logging
import json


LOG_MESSAGES = {
    "PathNotFound": "The file path does not exist.",
    "UnreadableFile": "The file was not readable.",
    "MalformedJson": "The trigger(s) definition has malformed JSON.",
    "InvalidType": "The trigger definition is an invalid input type.",
    "InvalidAutotagDims": "The autotag could not be evaluated because of a dimension mismatch.",
    "InvalidSCQLSyntax": "The trigger definition is valid JSON but has invalid SCQL.",
    "IncompleteTriggerState": "A required field to evaluate the trigger is missing.",
}

_LogRecordDefaultAttributes = {
    "name",
    "msg",
    "args",
    "levelname",
    "levelno",
    "pathname",
    "filename",
    "module",
    "exc_info",
    "exc_text",
    "stack_info",
    "lineno",
    "funcName",
    "created",
    "msecs",
    "relativeCreated",
    "thread",
    "threadName",
    "processName",
    "process",
    "message",
    "asctime",
}

BASIC_FORMAT = {
    "timestamp": "asctime",
}


class PercentStyle(object):

    asctime_format = "%(asctime)s"
    asctime_search = "%(asctime)"

    def __init__(self):
        self._fmt = ""

    def usesTime(self):
        return self._fmt.find(self.asctime_search) >= 0

    def format(self, record):
        return self._fmt % record.__dict__


class JsonFormatter(logging.Formatter):
    """
    Converts a LogRecord to a JSON string.
    """

    def __init__(
        self,
        fmt: dict = BASIC_FORMAT,
        style: str = "%",
        datefmt: str = "%Y-%m-%dT%H:%M:%S%Z",
    ):
        logging.Formatter.__init__(self, fmt="", datefmt=datefmt, style=style)

        self.json_fmt = fmt
        self._style = PercentStyle()
        self._style._fmt = ""

    def setRecordMessage(self, record: logging.LogRecord) -> None:
        if isinstance(record.msg, (int, float, bool, type(None))):
            # keep these types without quote when output
            record.message = record.msg
        else:
            record.message = str(record.msg)

        if record.args:
            record.message = record.getMessage()

        if record.exc_info and not record.exc_text:
            record.exc_text = self.formatException(record.exc_info)

        def _add_newline_if_missing(message):
            message = str(message)
            if message[-1:] != "\n":
                message += "\n"
            return message

        if record.exc_text:
            record.message = _add_newline_if_missing(record.message)
            record.message += record.exc_text
        if getattr(record, "stack_info", None):
            record.message = _add_newline_if_missing(record.message)
            record.message += self.formatStack(record.stack_info)

    def getRecordExtraAttrs(self, record: logging.LogRecord) -> dict:
        extras = {
            k: record.__dict__[k]
            for k in record.__dict__
            if k not in _LogRecordDefaultAttributes
        }
        return extras

    def formatMessage(self, record: logging.LogRecord) -> str:
        return self._style.format(record)

    def format(self, record: logging.LogRecord) -> str:
        def _set_extra_to_result():
            for k, v in extra.items():
                if k not in self.json_fmt:
                    result[k] = v

        def _set_fmt_to_result():
            if v in record.__dict__:
                result[k] = getattr(record, v, None)
            else:
                self._style._fmt = v
                result[k] = self.formatMessage(record)

        result = {}

        self.setRecordMessage(record)

        record.asctime = self.formatTime(record, self.datefmt)

        extra = record.__dict__.pop("__extra", None) or record.__dict__.pop(
            "_JsonFormatter__extra", None
        )
        if extra is None:
            extra = self.getRecordExtraAttrs(record)

        for k, v in self.json_fmt.items():
            if k in extra:
                result[k] = extra[k]
            else:
                _set_fmt_to_result()
        _set_extra_to_result()

        record.__extra = extra

        return json.dumps(result)


class Logger:
    def __init__(self, name: str, filename: str) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        formatter = JsonFormatter()

        sh = logging.FileHandler(filename)
        sh.setFormatter(formatter)

        self.logger.addHandler(sh)

    def get_extras(self, type: str, message: str, extra: dict = {}) -> dict:
        log_info = {"message": message}
        if extra.get("log_info"):
            log_info.update(extra.get("log_info"))
            del extra["log_info"]
        extras = {"type": type, "log_info": log_info}
        extras.update(extra)
        return extras

    def info(self, message: str, extra: dict = {}) -> None:
        extras = self.get_extras("INFO", message, extra)
        self.logger.info(
            message,
            extra=extras,
        )

    def warn(self, message: str, extra: dict = {}) -> None:
        extras = self.get_extras("WARN", message, extra)
        self.logger.warning(
            message,
            extra=extras,
        )

    def error(self, message: str, extra: dict = {}) -> None:
        extras = self.get_extras("ERROR", message, extra)
        self.logger.error(
            message,
            extra=extras,
        )
