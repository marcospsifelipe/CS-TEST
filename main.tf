# Infraestrutura como código com configuração insegura
# Usado para simular análise de IaC (Infrastructure as Code)

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "b" {
  bucket = "my-open-bucket-test"
  acl    = "public-read"  # vulnerabilidade: bucket público
}
