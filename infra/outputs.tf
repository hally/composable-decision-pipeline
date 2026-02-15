output "aws_region" {
  value       = var.aws_region
  description = "Region configured for this deployment"
}

output "api_base_url" {
  value       = aws_apigatewayv2_api.http_api.api_endpoint
  description = "Base URL for the HTTP API"
}
