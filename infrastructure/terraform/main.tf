terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  # Region will be configured via AWS_REGION environment variable
}

# DynamoDB Tables
resource "aws_dynamodb_table" "transactions" {
  name           = "budget-app-transactions"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  range_key      = "user_id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "user_id"
    type = "S"
  }

  tags = {
    Environment = "production"
    Application = "budget-app"
  }
}

resource "aws_dynamodb_table" "budgets" {
  name           = "budget-app-budgets"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  range_key      = "user_id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "user_id"
    type = "S"
  }

  tags = {
    Environment = "production"
    Application = "budget-app"
  }
}

# Lambda Function
resource "aws_lambda_function" "budget_api" {
  filename         = "../backend/budget_api.zip"
  function_name    = "budget-app-api"
  role            = aws_iam_role.lambda_exec.arn
  handler         = "app.main.handler"
  runtime         = "python3.10"

  environment {
    variables = {
      DATABASE_URL = var.database_url
    }
  }
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_exec" {
  name = "budget_app_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# API Gateway
resource "aws_apigatewayv2_api" "budget_api" {
  name          = "budget-app-api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "budget_api" {
  api_id = aws_apigatewayv2_api.budget_api.id
  name   = "prod"
  auto_deploy = true
}

resource "aws_apigatewayv2_integration" "budget_api" {
  api_id           = aws_apigatewayv2_api.budget_api.id
  integration_type = "AWS_PROXY"

  connection_type    = "INTERNET"
  description        = "Lambda integration"
  integration_method = "POST"
  integration_uri    = aws_lambda_function.budget_api.invoke_arn
}

resource "aws_apigatewayv2_route" "budget_api" {
  api_id    = aws_apigatewayv2_api.budget_api.id
  route_key = "ANY /{proxy+}"
  target    = "integrations/${aws_apigatewayv2_integration.budget_api.id}"
}

# Lambda permission for API Gateway
resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.budget_api.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.budget_api.execution_arn}/*/*"
}
