from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import registry

from expense_tracker.models import Expense
from expense_tracker.tables import expense_table

_registry = registry()


def map_tables_to_entities() -> None:
    _registry.map_imperatively(Expense, expense_table)


def create_tables(bind: Engine) -> None:
    expense_table.create(bind, checkfirst=True)
