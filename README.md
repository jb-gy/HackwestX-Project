# Budget Planning Application

A full-stack budget planning application that helps users track expenses, manage budgets, and visualize spending patterns.


PS: This codebase in incomplete, and only covers the scope of my contributions to the project.

## Features

- 📊 Real-time budget tracking and visualization
- 💰 Category-based expense management
- 📈 Progress tracking for budget categories
- 🔄 Dynamic updates with toast notifications
- 🔗 Plaid API integration for secure bank account linking
- 📊 Transaction fetching and management
- 📱 Responsive design with modern UI

## Tech Stack

### Frontend
- **React** with TypeScript for the user interface
- **Chakra UI** for component styling and theming
- **React Hooks** for state management
- **Custom Theme**: Tailored color palette and global styles
- Components:
  - BudgetPlanner: Manages budget categories and spending with dynamic updates
  - ExpenseChart: Visualizes spending patterns using Recharts
  - TransactionSummary: Displays transaction history with Plaid integration
  - DashboardLayout: Main application layout for consistent UI

### Backend
- **FastAPI** framework for API development
- **Python 3.10** runtime
- **SQLAlchemy** for database ORM
- **Mangum** for AWS Lambda integration
- **Plaid API** integration for financial data
- **CORS** middleware enabled for frontend integration

### Infrastructure (AWS)
- **Lambda** for serverless backend deployment
- **API Gateway** (HTTP API) for REST endpoint management
- **DynamoDB** tables:
  - `budget-app-transactions`: Stores transaction records
  - `budget-app-budgets`: Stores budget configurations
- **Terraform** for Infrastructure as Code

## API Endpoints

Base URL: `/api/v1`

### Transactions
- `GET /api/v1/transactions`: List transactions
- `POST /api/v1/transactions`: Create new transaction
- `GET /api/v1/budgets`: List budgets
- `POST /api/v1/budgets`: Create new budget
- `GET /api/v1/budgets/summary`: Get budget summary

### Plaid Integration
The application integrates with the Plaid API to securely link bank accounts and fetch transaction data. The following endpoints are available for Plaid integration:

- `POST /create_link_token`: Create a Plaid link token for initializing Plaid Link. This token is used to securely link a user's bank account.
- `POST /exchange_token`: Exchange a public token received from Plaid Link for an access token. This access token is used to access the user's financial data.
- `GET /accounts/{access_token}`: Retrieve accounts associated with the given access token. This endpoint provides details about the user's linked bank accounts.
- `GET /transactions/{access_token}`: Fetch transactions for a specified date range using the access token. This endpoint allows the application to synchronize transaction data with the user's bank account.

### Transaction Synchronization and Budget Tracking
The application synchronizes transactions from Plaid and processes them to update budget tracking. The workflow involves:
- Fetching transactions using the Plaid API and storing them in the database.
- Calculating budget summaries by aggregating transaction amounts within specified budget periods. This involves filtering transactions by category and date range, and summing amounts to determine spending against budgeted amounts.
- Providing real-time updates to the frontend for dynamic budget management, allowing users to see their spending progress and adjust budgets as needed.

### Health Check
- `GET /healthz`: API health check endpoint

## Database Schema

### SQLAlchemy Models

#### Transactions Model
```python
{
  id: Integer (Primary Key)
  user_id: Integer (Foreign Key)
  amount: Float
  category: String
  date: DateTime
}
```

#### Budgets Model
```python
{
  id: Integer (Primary Key)
  user_id: Integer (Foreign Key)
  category: String
  amount: Float
  period_start: DateTime
  period_end: DateTime
}
```

## Setup and Deployment

### Prerequisites
- Node.js and npm/yarn
- Python 3.10
- AWS CLI configured
- Terraform

### Frontend Setup
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start development server:
   ```bash
   npm start
   ```

### Backend Setup
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run development server:
   ```bash
   uvicorn main:app --reload
   ```

### Infrastructure Deployment
1. Initialize Terraform:
   ```bash
   terraform init
   ```
2. Plan deployment:
   ```bash
   terraform plan
   ```
3. Apply infrastructure:
   ```bash
   terraform apply
   ```

### Terraform Outputs
- `api_endpoint`: API Gateway endpoint URL
- `lambda_function_name`: Name of the Lambda function
- `dynamodb_transactions_table`: Name of the DynamoDB transactions table
- `dynamodb_budgets_table`: Name of the DynamoDB budgets table

## Environment Variables

### Backend
- `DATABASE_URL`: PostgreSQL connection string
- `AWS_REGION`: AWS region for services
- `PLAID_CLIENT_ID`: Plaid API client ID
- `PLAID_SECRET`: Plaid API secret
- `PLAID_ENV`: Plaid environment (sandbox, development, or production)

## Security

- API Gateway routes configured for ANY /{proxy+}
- CORS enabled for development
- IAM roles configured for Lambda execution
- DynamoDB tables use on-demand capacity mode

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request



