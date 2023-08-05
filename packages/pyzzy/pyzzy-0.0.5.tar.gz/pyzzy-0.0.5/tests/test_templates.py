from pyzzy.utils.templates import render


data = {
    "test1": "{{ __private }}",
    "test2": "{{ public }}",
    "test3": "{{ node1[1].node2[2].node3[-1] }}",
    "test4": "{{ node1/1/node2/2/node3/-1 }}",
}

context = {
    "__private": "invalid key",
    "public": "valid key",

    "node1": [
        "element_1",
        {

            "node2": [
                "element_2",
                "element_3",
                {

                    "node3": [
                        "element_4",
                        "element_5",
                        "element_6"
                    ]
                }
            ]
        }
    ],
}


def test_render_1():
    assert render(data["test1"], context) == "{{ __private }}"


def test_render_2():
    assert render(data["test2"], context) == "valid key"


def test_render_3():
    assert render(data["test3"], context) == "element_6"


def test_render_4():
    assert render(data["test4"], context) == "element_6"


def test_render():
    tests = (
        ("render_1", test_render_1),
        ("render_2", test_render_2),
        ("render_3", test_render_3),
        ("render_4", test_render_4),
    )

    for func_name, func in tests:
        print("[*] Testing %s()..." % func_name)
        func()


if __name__ == "__main__":
    test_render()
