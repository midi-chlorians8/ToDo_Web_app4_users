# ToDo Web App for Users

Our service allows users to create and manage notes with ease. You can easily register and login to start creating notes. With our service, you can create new notes or delete old ones with just a few clicks.

## Tech Stack

This project uses the following technologies:

### Necessary:
- Python 3.10 - The programming language used for the backend.
- FastAPI 0.89.1 - The web framework used for the backend.
- HTML, CSS, and JavaScript - The front-end languages used to create the user interface.

### Not necessary:
- [Terraform](https://www.terraform.io/) - Terraform v1.4.4 Cloud enables infrastructure automation for provisioning!
- [AWS cloud](https://aws.amazon.com/what-is-aws/) - I use ec2 instance, elastic ip, ECR in AWS cloud 
- [GitHub Actions](https://github.com/features/actions)- GitHub Actions is a CI/CD platform that allows you to automate your software development workflows right in your repository. 

## Running the project locally

1. Fork/Clone

1. Install python venv:

    ```sh
    apt install python3.10-venv
    ```

1. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Run the app:

    ```sh
    (venv)$ python main.py
    ```

1. Test at [http://localhost:8081/docs](http://localhost:8081/docs)

### To start the program in the background, use this command:
```sh
nohup python main.py &
```

To stop:
```sh
ps aux | grep main.py
```
```sh
kill <PID>
```
## Deploying the project to AWS
Login to AWS cloud (I use linux in local machine):

```sh
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
```
Terraform commands:
To store tfstate on remote s3 bucket comment that code:
```sh
/*
terraform {
  backend "s3" {
    bucket = "my-tf-state-bucket-gelding-dev" #Change bucket name to your actual bucket name. You will see that in outputs.
    key    = "path/to/my/key"
    region = "eu-central-1"
  }
}
*/
```

Key KeyFromLinuxAWS-Frankfurt already have been created in AWS account 
```sh
terraform init
```

```sh
terraform apply --auto-approve
```

To store tfstate on remote s3 bucket UNlock that code:
```sh
terraform {
  backend "s3" {
    bucket = "my-tf-state-bucket-gelding-dev" #Change bucket name to your actual bucket name. You will see that in outputs.
    key    = "path/to/my/key"
    region = "eu-central-1"
  }
}
```

Change harcoded bucket and region. (new bucket name will be in outputs)
Example: bucket_name = "my-tf-state-bucket-gorilla-prod"

```sh
terraform init -migrate-state
```
I go to the server and manually *Check. I added that step in init scypt. Maybe manual don't need to do that.
sudo chown ubuntu ToDo_Web_app3/

Manual go to the instance and connect to ECR. *It can be automated in terraform.
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 734075410113.dkr.ecr.eu-central-1.amazonaws.com

Next I setup CI/CD creds:
Go to AWS -> IAM -> users -> ecr-user
Open Security credentials tab
Scroll down to Access keys -> Create access key -> Other
Save file.
Add Secret to github action secret store. *In the future we check availabilit terraform add secrets to github.




Then we add policy to user ecr user 
AWSAppRunnerServicePolicyForECRAccess, 
EC2InstanceProfileForImageBuilderECRContainerBuilds,
ecretsManagerReadWrite
* In the future we need to improve that





Start scypt to add ssl serts:
```sh
./init-letsencrypt.sh
```

## To setup CI/CD we need to add secret vars::

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- ECR_REPOSITORY
- INSTANCE_HOST
- INSTANCE_KEY
- INSTANCE_USER

These variables are used in our GitHub Actions pipeline.
![image](https://user-images.githubusercontent.com/50805334/224275693-42f42348-d12f-459b-b8a5-8d67ecbfe11d.png)


To delete all:
we need to do some steps manually
1) Delete ECR registry: aws ecr delete-repository --repository-name fastapi-backend-repository-dev --force --region eu-central-1

## Helpful Hints

- If some port is already busy (tested on Ubuntu): `sudo fuser -k 8000/tcp`
- To clear all container images volumes: `sudo docker system prune -a --volumes`
- To stop all running containers: `sudo docker stop $(sudo docker ps -aq)`
- To remove all containers (this will not delete any data volumes): `sudo docker rm $(sudo docker ps -aq)`
- To build weithout dependenses: `docker-compose build --no-cache`


## Links

- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/10.4/usage/flow/)
- [Testdriven.io - FastAPI JWT Auth](https://testdriven.io/blog/fastapi-jwt-auth/)
- [GitHub - Testdriven.io FastAPI JWT](https://github.com/testdrivenio/fastapi-jwt)
- [Securing FastAPI with JWT Token-based Authentication](https://testdriven.io/blog/fastapi-jwt-auth/)



## Setting up HTTPS Certificates

1. Uncomment nginx and certbot in docker-compose.
2. Switch to root user: `sudo su`
3. Edit files `init-letsencrypt.sh` and `data/nginx/app.conf`, replacing the server's DNS name with the actual DNS name.
4. Run the script to set up Let's Encrypt certificates: `./init-letsencrypt.sh`
5. Uncomment the following lines in the Nginx configuration:

uncomment:
upstream fastapi {
       server web:8000;
}
    location / {
        proxy_pass http://fastapi;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }  

6. Reload Nginx configuration: `docker-compose exec nginx nginx -s reload`



DataBase observability:
If you start app fastapi with docker-compose:
change that row in .env
SQLALCHEMY_DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres

If you start app fastapi local:
change that row in .env
SQLALCHEMY_DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres

Migration command:
alembic upgrade heads