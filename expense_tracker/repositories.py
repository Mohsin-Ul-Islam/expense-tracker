from typing import List, Optional

from sqlalchemy.orm import Session

from expense_tracker.models import Expense


class SQLAlchemyExpenseRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, ident: str) -> Optional[Expense]:
        return self.session.query(Expense).get(ident)

    def list_(self) -> List[Expense]:
        return self.session.query(Expense).all()

    def add(self, expense: Expense) -> None:
        self.session.add(expense)
