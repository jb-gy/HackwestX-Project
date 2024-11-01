variable "database_url" {
  description = "PostgreSQL database URL"
  type        = string
}

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-west-2"
}
