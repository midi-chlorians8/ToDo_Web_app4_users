data "aws_ami" "ubuntu" {
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server*"] 
  }

  most_recent = true
  owners = ["099720109477"] # Canonical
}


resource "aws_security_group" "example" {
  name        = "todo_terraform_sg-${random_pet.bucket_name.id}-${var.tags.Environment}"
  description = "Allow SSH and HTTP/HTTPS traffic"

  dynamic "ingress" {
    for_each = var.allow_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }  
  tags = var.tags
}










# Create an IAM role for EC2 with full access to ECR
resource "aws_iam_role" "ec2_role" {
  name = "ec2_role-${random_pet.bucket_name.id}-${var.tags.Environment}"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Attach the AWS managed policy for ECR full access to the role
resource "aws_iam_role_policy_attachment" "ecr_full_access" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess"
}

resource "aws_instance" "my_serv_todo" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type #"t3.micro"

  key_name      = var.key_name
  security_groups = [aws_security_group.example.name]

  user_data = "${file("install_awscli_docker.sh")}"

  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  tags = merge(var.tags, {"Name" = "ToDo-instance-${var.tags.Environment}"})
}

# Create an IAM instance profile for the EC2 instance
resource "aws_iam_instance_profile" "ec2_profile" {
  name = aws_iam_role.ec2_role.name
  role = aws_iam_role.ec2_role.name
}














resource "aws_eip" "example" {
  vpc = true
}

output "public_ip" {
  description = "Contains the public(elastic) IP address"
  value       = aws_eip.example.public_ip
}


resource "aws_eip_association" "eip_assoc" {
  instance_id = aws_instance.my_serv_todo.id
  allocation_id         = aws_eip.example.id
}