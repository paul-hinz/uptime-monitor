resource "aws_s3_bucket" "deploy_bucket" {
  bucket = "${var.app_name}-deploy-bucket"
  force_destroy = true
}

resource "aws_s3_object" "app_version_zip" {
  bucket = aws_s3_bucket.deploy_bucket.id
  key    = "uptime-monitor.zip"
  source = "${path.module}/../uptime-monitor.zip"
  etag   = filemd5("${path.module}/../uptime-monitor.zip")
}

resource "aws_elastic_beanstalk_application_version" "app_version" {
  name        = "uptime-monitor-v${timestamp()}"
  application = aws_elastic_beanstalk_application.app.name
  bucket      = aws_s3_bucket.deploy_bucket.bucket
  key         = aws_s3_object.app_version_zip.key

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_elastic_beanstalk_environment" "env" {
  name                = var.env_name
  application         = aws_elastic_beanstalk_application.app.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.5.1 running Docker"

  setting {
    namespace = "aws:elasticbeanstalk:environment"
    name      = "EnvironmentType"
    value     = "SingleInstance"
  }

  setting {
  namespace = "aws:autoscaling:launchconfiguration"
  name      = "IamInstanceProfile"
  value     = aws_iam_instance_profile.beanstalk_instance_profile.name
}

  version_label = aws_elastic_beanstalk_application_version.app_version.name
}