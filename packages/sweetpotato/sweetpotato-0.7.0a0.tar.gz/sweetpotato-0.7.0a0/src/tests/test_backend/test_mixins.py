import unittest


class TestJsComponentMixin(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_read_file(self) -> None:
        ...

    def test_read_string(self) -> None:
        ...

    def tearDown(self) -> None:
        ...


class TestPropsMixin(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_props(self) -> None:
        ...

    def tearDown(self) -> None:
        ...


if __name__ == "__main__":
    unittest.main()
