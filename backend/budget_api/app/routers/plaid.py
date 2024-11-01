from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, List
from datetime import datetime, timedelta
from ..database import get_db
from ..services.plaid_service import plaid_service

router = APIRouter()

@router.post("/create_link_token")
async def create_link_token(user_id: str):
    """Create a Link token for Plaid Link initialization"""
    try:
        link_token = await plaid_service.create_link_token(user_id)
        return link_token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/exchange_token")
async def exchange_public_token(public_token: str):
    """Exchange public token for access token"""
    try:
        tokens = await plaid_service.exchange_public_token(public_token)
        return tokens
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/accounts/{access_token}")
async def get_accounts(access_token: str):
    """Get accounts associated with an access token"""
    try:
        accounts = await plaid_service.get_accounts(access_token)
        return accounts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/transactions/{access_token}")
async def get_transactions(
    access_token: str,
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(get_db)
):
    """Get transactions for a date range"""
    try:
        if not start_date:
            start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        if not end_date:
            end_date = datetime.now().strftime("%Y-%m-%d")

        transactions = await plaid_service.get_transactions(
            access_token,
            datetime.strptime(start_date, "%Y-%m-%d"),
            datetime.strptime(end_date, "%Y-%m-%d")
        )
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
