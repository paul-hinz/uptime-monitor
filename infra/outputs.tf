output "app_name" {
  value = aws_elastic_beanstalk_application.app.name
}

output "environment_url" {
  value = aws_elastic_beanstalk_environment.env.endpoint_url
}