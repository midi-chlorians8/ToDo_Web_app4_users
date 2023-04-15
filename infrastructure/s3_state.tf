resource "random_pet" "bucket_name" {
  length = 1
  separator = "-"
}

resource "aws_s3_bucket" "bucket_tf_state" {
  bucket = "my-tf-state-bucket-${random_pet.bucket_name.id}-${var.tags.Environment}"
  versioning {
    enabled = true
  }

  tags = var.tags
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.bucket_tf_state.id
  acl    = "private"
}

resource "aws_dynamodb_table" "mytable" {
  name           = "mytable-${random_pet.bucket_name.id}-${var.tags.Environment}"
  hash_key       = "LockID"
  read_capacity  = 30
  write_capacity = 30

  attribute {
    name = "LockID"
    type = "S"
  }
}


output "bucket_name" {
  description = "Contains the public(elastic) IP address"
  value       = aws_s3_bucket.bucket_tf_state.bucket
}


terraform {
  backend "s3" {
    bucket = "my-tf-state-bucket-gorilla-prod" #aws_s3_bucket.bucket_tf_state.bucket #aws_s3_bucket.bucket_tf_state.id
    key    = "path/to/my/key"
    region = "eu-central-1"
  }
}
