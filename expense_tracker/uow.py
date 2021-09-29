from __future__ import annotations

from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from expense_tracker.repositories import SQLAlchemyExpenseRepository


class SQLAlchemyUnitOfWork:

    expenses: SQLAlchemyExpenseRepository
    session: Session
    engine: Engine

    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///local.db")
        self.session_factory = sessionmaker(bind=self.engine)

    def __enter__(self) -> SQLAlchemyUnitOfWork:
        self.session = self.session_factory()
        self.expenses = SQLAlchemyExpenseRepository(self.session)
        return self

    def __exit__(self, *_) -> None:
        self.session.commit()
        self.session.close()
