"""Test Suite for the SplitHandler"""
import logging
from logging import getLogger, Logger, LogRecord
from logging.handlers import QueueHandler
from queue import Queue
from unittest import TestCase

from log_splitter import SplitHandler


class TestSplitHandler(TestCase):
    """Test case for the SplitHandler class."""

    def assert_log(self, record: LogRecord, level: int, message: str) -> None:
        """Assert a LogRecord."""
        self.assertEqual(record.levelno, level,
                         f"Level not equal for {record}")
        self.assertEqual(record.msg, message,
                         f"Message not equal for {record}")
        self.assertEqual(record.name, __name__, f"Name not equal for {record}")

    def test_split_logs(self):
        """Test whteher the Split Handler correctly dispacth log records."""
        logger: Logger = getLogger(__name__)
        logger.setLevel(1)

        queue_1: Queue = Queue(3)
        queue_2: Queue = Queue(3)
        logger.addHandler(SplitHandler(
            handler_1=QueueHandler(queue_1),
            handler_2=QueueHandler(queue_2),
            log_level_threshold=logging.WARNING
        ))

        logger.log(3, "level3_log %s", "my_string")
        logger.debug("debug_log")
        logger.info("info_log")
        logger.warning("warn_log")
        logger.error("error_log")
        logger.critical("critical_log")

        self.assert_log(queue_1.get_nowait(), 3, "level3_log my_string")
        self.assert_log(queue_1.get_nowait(), logging.DEBUG, "debug_log")
        self.assert_log(queue_1.get_nowait(), logging.INFO, "info_log")
        self.assertTrue(queue_1.empty())

        self.assert_log(queue_2.get_nowait(), logging.WARNING, "warn_log")
        self.assert_log(queue_2.get_nowait(), logging.ERROR, "error_log")
        self.assert_log(queue_2.get_nowait(), logging.CRITICAL, "critical_log")
        self.assertTrue(queue_2.empty())
