from expense_tracker.models import Expense
from expense_tracker.uow import SQLAlchemyUnitOfWork


class CreateExpense:  # pylint: disable=too-few-public-methods
    def __init__(self, amount: float, uow: SQLAlchemyUnitOfWork) -> None:
        self.amount = amount
        self.uow = uow

    def execute(self) -> None:

        with self.uow as _uow:
            _uow.expenses.add(Expense(self.amount))
