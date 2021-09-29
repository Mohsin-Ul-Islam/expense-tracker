from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, Float, Table
from sqlalchemy.orm import registry

_registry = registry()

expense_table = Table(
    "expenses",
    _registry.metadata,
    Column("ident", BigInteger, nullable=False, primary_key=True),
    Column("amount", Float, nullable=False),
    Column("created_at", DateTime, default=datetime.now),
    Column("updated_at", DateTime, default=datetime.now, onupdate=datetime.now),
)
