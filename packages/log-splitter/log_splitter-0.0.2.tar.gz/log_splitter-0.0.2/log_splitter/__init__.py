"""
    Exposes one class, ``SplitHandler``, which takes two logging Handlers and
    split the log between them according to a log level threshold.
"""
from typing import Optional
from logging import LogRecord, Handler


class SplitHandler(Handler):
    """A logging Handler that splits your logs between two handlers.

    Attributes:
        handler_1: The handler that will receive log records which level is
                   below `log_level_threshold`.
        handler_1: The handler that will receive log records which level is
                   above or equal to `log_level_threshold`.
    """
    handler_1: Handler
    handler_2: Handler
    log_level_threshold: int

    def __init__(self,
                 handler_1: Handler,
                 handler_2: Handler,
                 log_level_threshold: int):
        super().__init__()
        self.handler_1 = handler_1
        self.handler_2 = handler_2
        self.log_level_threshold = log_level_threshold

    def emit(self, record: LogRecord) -> None:
        pass  # pragma: no cover

    def handle(self, record: LogRecord) -> Optional[LogRecord]:
        if record.levelno < self.log_level_threshold:
            handler = self.handler_1
        else:
            handler = self.handler_2

        return handler.handle(record)
