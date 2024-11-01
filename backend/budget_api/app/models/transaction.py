from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    date = Column(DateTime)
    plaid_transaction_id = Column(String, unique=True, nullable=True)

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    category = Column(String)
    amount = Column(Float)
    period_start = Column(DateTime)
    period_end = Column(DateTime)
