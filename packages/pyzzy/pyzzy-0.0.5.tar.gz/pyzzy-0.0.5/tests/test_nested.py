from pyzzy.utils import nested


DATA_SOURCE = {
    "key1": [
        {
            "key2": [
                {
                    "key3": "value1"
                }
            ]
        }
    ]
}


def test_nget():
    data = DATA_SOURCE
    proxy = nested.NProxy(data)
    expected = data["key1"][0]["key2"][-1]["key3"]
    result = proxy.nget("key1[0].key2[-1].key3")
    assert result == expected


def test_nget_raises():
    """Raise exception when key path is invalid and no default value is given"""
    data = {}
    proxy = nested.NProxy(data)
    try:
        proxy.nget("key1[0].key2[-1].key3", default=nested.UNSET)
    except nested.NestedOperationError:
        pass


def test_nget_default():
    """Get default value (None) when key path is invalid"""
    data = {}
    proxy = nested.NProxy(data)
    expected = None
    result = proxy.nget("key1[0].key2[-1].key3")  # default=None
    assert result == expected


def test_nget_getitem():
    data = DATA_SOURCE
    proxy = nested.NProxy(data)
    expected = data["key1"][0]["key2"][-1]["key3"]
    result = proxy["key1[0].key2[-1].key3"]
    assert result == expected


def test_nget_getitem_raises():
    """Raise exception when key path is invalid and no default value is given"""
    data = {}
    proxy = nested.NProxy(data)
    try:
        proxy["key1[0].key2[-1].key3"]
    except nested.NestedOperationError:
        pass


def test_nset():
    data = nested.ncopy(DATA_SOURCE)
    proxy = nested.NProxy(data)
    expected = "value2 (created)"
    proxy.nset("key1[0].key2[-1].key4", expected)
    result = data["key1"][0]["key2"][-1]["key4"]
    assert result == expected


def test_nset_raises():
    """Raise exception when key path is invalid"""
    data = {}
    proxy = nested.NProxy(data)
    try:
        proxy.nset("key1[0].key2[-1].key3", "value")
    except nested.NestedOperationError:
        pass


def test_nset_setitem():
    data = nested.ncopy(DATA_SOURCE)
    proxy = nested.NProxy(data)
    expected = "value2 (created)"
    proxy["key1[0].key2[-1].key4"] = expected
    result = data["key1"][0]["key2"][-1]["key4"]
    assert result == expected


def test_nset_setitem_raises():
    """Raise exception when key path is invalid"""
    data = {}
    proxy = nested.NProxy(data)
    try:
        proxy["key1[0].key2[-1].key3"] = "value"
    except nested.NestedOperationError:
        pass


def test_ndel():
    data = nested.ncopy(DATA_SOURCE)
    proxy = nested.NProxy(data)
    expected = {}
    proxy.ndel("key1[0].key2[-1].key3")
    result = data["key1"][0]["key2"][-1]
    assert result == expected


def test_ndel_raises():
    """Raise exception when key path is invalid"""
    data = {}
    proxy = nested.NProxy(data)
    try:
        proxy.ndel("key1[0].key2[-1].key3")
    except nested.NestedOperationError:
        pass


def test_ndel_delitem():
    data = nested.ncopy(DATA_SOURCE)
    proxy = nested.NProxy(data)
    expected = {}
    proxy.ndel("key1[0].key2[-1].key3")
    result = data["key1"][0]["key2"][-1]
    assert result == expected


def test_ndel_delitem_raises():
    """Raise exception when key path is invalid"""
    data = {}
    proxy = nested.NProxy(data)
    try:
        del proxy["key1[0].key2[-1].key3"]
    except nested.NestedOperationError:
        pass


def test_ncontains():
    data = nested.ncopy(DATA_SOURCE)
    proxy = nested.NProxy(data)
    expected = True
    result = "key1[0].key2[-1].key3" in proxy
    assert result == expected


def main():

    tests = (
        ("nget", test_nget),
        ("nget_raises", test_nget_raises),
        ("nget_default", test_nget_default),

        ("nset", test_nset),
        ("nset_raises", test_nset_raises),

        ("ndel", test_ndel),
        ("ndel_raises", test_ndel_raises),

        ("nget_getitem", test_nget_getitem),
        ("nget_getitem_raises", test_nget_getitem_raises),

        ("nset_setitem", test_nset_setitem),
        ("nset_setitem_raises", test_nset_setitem_raises),

        ("ndel_delitem", test_ndel_delitem),
        ("ndel_delitem_raises", test_ndel_delitem_raises),

        ("ncontains", test_ncontains),
    )

    for name, func in tests:
        print("[*] Testing %s()..." % name)
        func()


if __name__ == "__main__":
    main()
