from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


def ident_f() -> int:
    return uuid4().int >> 96


@dataclass
class Expense:

    ident: int = field(default_factory=ident_f, init=False, hash=True, compare=True)
    amount: float

    created_at: datetime = field(default_factory=datetime.now, init=False)
    updated_at: datetime = field(default_factory=datetime.now, init=False)
