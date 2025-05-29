output "db_endpoint" {
  description = "Endpoint da instância PostgreSQL"
  value       = aws_db_instance.postgres.endpoint
}

output "db_port" {
  description = "Porta do banco"
  value       = aws_db_instance.postgres.port
}
