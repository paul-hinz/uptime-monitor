provider "aws" {
  region = var.aws_region
}

resource "aws_elastic_beanstalk_application" "app" {
  name        = var.app_name
  description = "Uptime Monitor App"
}