provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket         = "uptime-monitor-paul"
    key            = "uptime-monitor/terraform.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}

resource "aws_elastic_beanstalk_application" "app" {
  name        = var.app_name
  description = "Uptime Monitor App"
}