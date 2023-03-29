# -ToDo_Web_app4_users
Test_proj_fastapi_users

Local start:
cd ./app
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt

cd ..
sudo docker-compose up -d db - Raise db on local ps

uvicorn main:app --reload



*
#uvicorn main:app --reload --port 8000

If some port already busy (test on ubuntu) = sudo fuser -k 8000/tcp
To clear all container images = sudo docker system prune -a --volumes


remember general flow:
https://fastapi-users.github.io/fastapi-users/10.4/usage/flow/

sources:
https://testdriven.io/blog/fastapi-jwt-auth/

https://github.com/testdrivenio/fastapi-jwt

Todo:
1) Copy foles from sql alchemy proj to here. +
2) Generate some html pages to login