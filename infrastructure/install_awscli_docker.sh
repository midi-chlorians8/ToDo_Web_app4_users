#!/bin/bash


# install aws cli to ECR connection
sudo apt install unzip -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
rm get-docker.sh



sudo usermod -aG docker ubuntu


sudo apt install --yes  python3-pip
sudo pip3 install docker-compose


cd /home/ubuntu
git clone https://github.com/midi-chlorians8/ToDo_Web_app4_users.git
chown ubuntu /home/ubuntu/ToDo_Web_app4_users
touch IamHer



chmod +x init-letsencrypt.sh

aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 734075410113.dkr.ecr.eu-central-1.amazonaws.com