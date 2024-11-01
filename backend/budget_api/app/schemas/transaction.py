from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    date: datetime
    plaid_transaction_id: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    user_id: str

    class Config:
        from_attributes = True

class BudgetBase(BaseModel):
    category: str
    amount: float
    period_start: datetime
    period_end: datetime

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    user_id: str

    class Config:
        from_attributes = True
