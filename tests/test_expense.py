from datetime import datetime
from unittest import TestCase, main

from expense_tracker.models import Expense


class TestExpense(TestCase):
    def test_expense_object_creation(self) -> None:

        breakfast = Expense(amount=100)

        self.assertIsInstance(breakfast, Expense)

        self.assertNotEqual(breakfast.ident, None)
        self.assertEqual(breakfast.amount, 100)
        self.assertEqual(breakfast.created_at.date(), datetime.now().date())
        self.assertEqual(breakfast.updated_at.date(), datetime.now().date())


if __name__ == "__main__":
    main()
