import collections
import sys


pyversion = 'PY%s%s' % sys.version_info[:2]


def get_data(factory=None):
    dict_factory = factory or collections.OrderedDict

    specials = dict_factory((
        ("deja-vu", "déjà vu"),
        ("multiline", "line1\nline2\nline3"),
    ))
    numbers = dict_factory((
        ('one', 1),
        ('two', 2),
        ('three', 3),
        ('four', 4),
        ('five', 5),
    ))
    datas = dict_factory((
        ('specials', specials),
        ('numbers', numbers),
    ))
    return datas


def obj2str(var, indent=0):

    items = var.items() if isinstance(var, collections.abc.Mapping) else var

    # Python < 3.6 doesn't preserve order so at least,
    # sort the pairs to allow check on value
    if sys.version_info < (3, 6) and isinstance(var, collections.abc.Mapping):
        items = sorted(items, key=lambda item: item[0])

    key_len = max(len(('%s:' % k)) for k, v in items)
    prefix = ' ' * 4
    frmt = '\n%s%s %s'

    lines = ''
    for key, value in items:
        key = ('%s:' % key).ljust(key_len)
        if isinstance(value, (collections.abc.Mapping, list, tuple)):
            value = '\n%s%s' % (prefix, obj2str(value, indent + 1))
        lines += frmt % (prefix * indent, key, value)

    return lines.strip()


def use_logger(logger):
    message = 'The quick brown fox jumps over the lazy dog'
    methods = [
        'critical',
        'error',
        'warning',
        'fail',
        'success',
        'info',
        'debug',
    ]

    for method_name in methods:
        log_method = getattr(logger, method_name, None)
        if log_method:
            log_method(message)


def logger_infos(logger):
    fmt = "logger='%s' (level=%d, %s handlers)"
    name = getattr(logger, 'name', '')
    print(fmt % (name, logger.level, len(logger.handlers)))

    fmt = '  \__ %s (level=%d)'
    for handler in logger.handlers:
        print(fmt % (handler.__class__.__name__, handler.level))
