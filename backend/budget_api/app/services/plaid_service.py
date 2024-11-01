from datetime import datetime, timedelta
import random
from typing import List, Dict, Any
import uuid

class MockPlaidService:
    """
    Mock implementation of Plaid service for development and testing.
    Will be replaced with real Plaid integration when credentials are available.
    """

    def __init__(self):
        self._mock_accounts = {}
        self._mock_transactions = {}

    async def create_link_token(self, user_id: str) -> Dict[str, str]:
        """Simulate creating a Plaid Link token"""
        return {
            "link_token": f"mock-link-token-{uuid.uuid4()}",
            "expiration": (datetime.now() + timedelta(hours=4)).isoformat()
        }

    async def exchange_public_token(self, public_token: str) -> Dict[str, str]:
        """Simulate exchanging public token for access token"""
        return {
            "access_token": f"mock-access-token-{uuid.uuid4()}",
            "item_id": f"mock-item-{uuid.uuid4()}"
        }

    async def get_accounts(self, access_token: str) -> List[Dict[str, Any]]:
        """Return mock bank accounts"""
        if access_token not in self._mock_accounts:
            self._mock_accounts[access_token] = [
                {
                    "account_id": f"acc-{uuid.uuid4()}",
                    "name": "Mock Checking",
                    "type": "depository",
                    "subtype": "checking",
                    "balances": {
                        "current": round(random.uniform(1000, 5000), 2),
                        "available": round(random.uniform(800, 4800), 2)
                    }
                },
                {
                    "account_id": f"acc-{uuid.uuid4()}",
                    "name": "Mock Savings",
                    "type": "depository",
                    "subtype": "savings",
                    "balances": {
                        "current": round(random.uniform(5000, 15000), 2),
                        "available": round(random.uniform(4800, 14800), 2)
                    }
                }
            ]
        return self._mock_accounts[access_token]

    async def get_transactions(self, access_token: str, start_date: datetime, end_date: datetime) -> List[Dict[str, Any]]:
        """Return mock transactions"""
        if access_token not in self._mock_transactions:
            categories = [
                "Food and Drink", "Shopping", "Transportation",
                "Entertainment", "Utilities", "Rent", "Healthcare"
            ]
            merchants = {
                "Food and Drink": ["Grocery Store", "Restaurant", "Coffee Shop"],
                "Shopping": ["Amazon", "Target", "Walmart"],
                "Transportation": ["Uber", "Gas Station", "Public Transit"],
                "Entertainment": ["Netflix", "Movie Theater", "Spotify"],
                "Utilities": ["Electric Company", "Water Service", "Internet Provider"],
                "Rent": ["Apartment Complex"],
                "Healthcare": ["Pharmacy", "Doctor's Office", "Health Insurance"]
            }

            transactions = []
            current_date = end_date
            while current_date >= start_date:
                # Generate 1-3 transactions per day
                for _ in range(random.randint(1, 3)):
                    category = random.choice(categories)
                    merchant = random.choice(merchants[category])
                    amount = round(random.uniform(5, 200), 2)

                    transactions.append({
                        "transaction_id": f"tx-{uuid.uuid4()}",
                        "account_id": self._mock_accounts[access_token][0]["account_id"],
                        "amount": amount,
                        "category": [category],
                        "date": current_date.strftime("%Y-%m-%d"),
                        "merchant_name": merchant,
                        "name": f"{merchant} - {category}",
                        "pending": False
                    })
                current_date -= timedelta(days=1)

            self._mock_transactions[access_token] = transactions

        return self._mock_transactions[access_token]

# Singleton instance
plaid_service = MockPlaidService()
