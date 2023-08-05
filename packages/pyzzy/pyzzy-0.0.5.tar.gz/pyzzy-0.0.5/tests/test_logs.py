import contextlib
import io
import logging
import time

import _pytest.logging
import pytest

import pyzzy as pz


@contextlib.contextmanager
def capture_handler_stream(logger, handler_name):
    handler = get_handler_by_name(logger.handlers, handler_name)
    old_stream = handler.stream
    new_stream = io.StringIO()
    handler.stream = new_stream
    try:
        yield new_stream
    finally:
        new_stream.close()
        handler.stream = old_stream


def get_handler_by_name(handlers, name):
    for handler in handlers:
        if handler.get_name() == name:
            return handler


@pytest.fixture()
def logging_config():
    logging.config.dictConfig(pz.logs.DEFAULT_CONFIG)
    return pz.logs.DEFAULT_CONFIG


def test_root_handlers_names(logging_config):
    logger = logging.getLogger()
    root_handlers_names = [
        h.get_name() for h in logger.handlers
        if not isinstance(h, _pytest.logging.LogCaptureHandler)
    ]
    assert root_handlers_names == ['console_production', 'tr_file']


def test_root_console_handler_output(logging_config):
    logger = logging.getLogger()
    message = "Log message"

    with capture_handler_stream(logger, "console_production") as stream:
        logger.error(message)
        logger.debug(message)
        captured_output = stream.getvalue()

    assert message in captured_output
    assert pz.logs.vars._colored_tags[logging.ERROR] in captured_output
    assert pz.logs.vars._colored_tags[logging.DEBUG] not in captured_output


def test_root_trfile_handler_output(logging_config):
    logger = logging.getLogger()
    message = "Log message"

    with capture_handler_stream(logger, "tr_file") as stream:
        logger.error(message)
        logger.debug(message)
        captured_output = stream.getvalue()

    assert message in captured_output
    assert logging._levelToName[logging.ERROR] in captured_output
    assert logging._levelToName[logging.DEBUG] in captured_output
    assert time.strftime('%Y-%m-%d %H:%M') in captured_output
    assert logger.name in captured_output


def main():
    logging_config_ = logging_config()
    test_root_handlers_names(logging_config_)
    test_root_console_handler_output(logging_config_)
    test_root_trfile_handler_output(logging_config_)


if __name__ == "__main__":
    main()
