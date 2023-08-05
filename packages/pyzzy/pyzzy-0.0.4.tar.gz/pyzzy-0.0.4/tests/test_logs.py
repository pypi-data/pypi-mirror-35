import logging

import pyzzy as pz


def test_init_logging():
    pz.init_logging(
        config=pz.logs.vars.DEFAULT_CONFIG,
        capture_warnings=True,
        simple_warnings=True,
        raise_exceptions=True,
    )


def test_handler_console_production(caplog):
    caplog.clear()

    logger = logging.getLogger('production')
    logger.propagate = True

    handler = get_handler_by_name(logger.handlers, 'console_production')
    formatter = handler.formatter

    log_fmt = formatter._fmt
    log_msg = "Log message"
    log_tags = pz.logs.vars._colored_tags

    all_levels = logging._levelToName.keys()
    test_levels = [lvl for lvl in all_levels if lvl >= handler.level]
    expected_levels = logging.CRITICAL, logging.ERROR, logging.WARNING

    for level_number in sorted(test_levels):
        logger.log(level_number, log_msg)

    result = [
        formatter.format(record)
        for record in caplog.records
    ]

    expected = [
        log_fmt % {'message': log_msg, 'levelname': log_tags[level]}
        for level in sorted(expected_levels)
    ]

    assert result == expected


def get_handler_by_name(handlers, name):
    for handler in handlers:
        if handler.get_name() == name:
            return handler
