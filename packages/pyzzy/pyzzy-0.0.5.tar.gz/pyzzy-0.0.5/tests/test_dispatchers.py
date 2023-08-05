from collections.abc import MutableMapping, MutableSequence
from pyzzy.utils.dispatchers import predicate_dispatch


def is_mapping(var):
    return isinstance(var, MutableMapping)


def is_sequence(var):
    return isinstance(var, MutableSequence)


@predicate_dispatch
def uppercase(var):
    return str(var).upper()


@uppercase.register(is_mapping)
def uppercase_on_mapping(mapping):
    return type(mapping)(
        (uppercase(k), uppercase(v)) for k, v in mapping.items()
    )


@uppercase.register(is_sequence)
def uppercase_on_sequence(sequence):
    return type(sequence)(uppercase(val) for val in sequence)


def test_uppercase_string():
    print("[*] Testing uppercase_string()...")
    string_sample = "abcdefghijklmnop"
    assert uppercase(string_sample) == "ABCDEFGHIJKLMNOP"


def test_uppercase_dict():
    print("[*] Testing uppercase_dict()...")
    dict_sample = {"abcd": "efgh", "ijkl": "mnop"}
    assert uppercase(dict_sample) == {"ABCD": "EFGH", "IJKL": "MNOP"}


def test_uppercase_list():
    print("[*] Testing uppercase_list()...")
    list_sample = ["abcd", "efgh", "ijkl", "mnop"]
    assert uppercase(list_sample) == ["ABCD", "EFGH", "IJKL", "MNOP"]


def test_uppercase_integer():
    print("[*] Testing uppercase_integer()...")
    integer_sample = 123456789
    assert uppercase(integer_sample) == "123456789"


def main():
    test_uppercase_string()
    test_uppercase_list()
    test_uppercase_dict()
    test_uppercase_integer()


if __name__ == "__main__":
    main()
