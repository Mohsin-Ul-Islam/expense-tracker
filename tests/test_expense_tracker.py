from unittest import TestCase, main

from expense_tracker import __version__


class TestExpenseTracker(TestCase):
    def test_version(self):
        assert __version__ == "0.1.0"


if __name__ == "__main__":
    main()
