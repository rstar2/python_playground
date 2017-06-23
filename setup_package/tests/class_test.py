# All 'test_' prefixed methods inside Test prefixed test classes
# (without an __init__ method) will be run by pytest by convention


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')