output "api_endpoint" {
  description = "API Gateway endpoint URL"
  value       = aws_apigatewayv2_stage.budget_api.invoke_url
}

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.budget_api.function_name
}

output "dynamodb_transactions_table" {
  description = "Name of the DynamoDB transactions table"
  value       = aws_dynamodb_table.transactions.name
}

output "dynamodb_budgets_table" {
  description = "Name of the DynamoDB budgets table"
  value       = aws_dynamodb_table.budgets.name
}
