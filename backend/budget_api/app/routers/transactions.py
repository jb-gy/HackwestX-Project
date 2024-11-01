from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.transaction import Transaction, Budget
from ..schemas.transaction import TransactionCreate, Transaction as TransactionSchema
from ..schemas.transaction import BudgetCreate, Budget as BudgetSchema
from datetime import datetime

router = APIRouter()

@router.post("/transactions/", response_model=TransactionSchema)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/transactions/", response_model=List[TransactionSchema])
def get_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).offset(skip).limit(limit).all()
    return transactions

@router.post("/budgets/", response_model=BudgetSchema)
def create_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    db_budget = Budget(**budget.dict())
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

@router.get("/budgets/", response_model=List[BudgetSchema])
def get_budgets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    budgets = db.query(Budget).offset(skip).limit(limit).all()
    return budgets

@router.get("/budgets/summary/")
def get_budget_summary(db: Session = Depends(get_db)):
    budgets = db.query(Budget).all()
    transactions = db.query(Transaction).all()

    summary = {}
    for budget in budgets:
        category = budget.category
        summary[category] = {
            "budget": budget.amount,
            "spent": sum(t.amount for t in transactions
                        if t.category == category
                        and budget.period_start <= t.date <= budget.period_end)
        }
    return summary
