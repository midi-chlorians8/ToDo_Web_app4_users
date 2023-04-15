resource "aws_iam_user" "ecr_user" {
  name = "ecr-user-${random_pet.bucket_name.id}-${var.tags.Environment}"
  tags = var.tags
}

resource "aws_iam_access_key" "ecr_user_key" {
  user = aws_iam_user.ecr_user.name
}

resource "aws_iam_user_policy" "ecr_user_policy" {
  name = "ecr-user-policy"
  user = aws_iam_user.ecr_user.name

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:GetRepositoryPolicy",
        "ecr:DescribeRepositories",
        "ecr:ListImages",
        "ecr:DescribeImages",
        "ecr:BatchGetImage"
      ],
      
      "Resource": "*"
    }
  ]
}
EOF
}

resource aws_ecr_repository ecr_repo {
  name                 = "fastapi-backend-repository-${random_pet.bucket_name.id}-${var.tags.Environment}"
  image_tag_mutability = "MUTABLE"
  
  # Optional arguments:
  
  # encryption_configuration - (Optional) Encryption configuration for the repository. See Encryption Configuration below for more details.
  
  # image_scanning_configuration - (Optional) Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See Image Scanning Configuration below for more details.
  
  # kms_key - (Optional) The ARN of the KMS key to use when encrypting the images in the repository. If not specified, uses the default AWS managed key for ECR.
}