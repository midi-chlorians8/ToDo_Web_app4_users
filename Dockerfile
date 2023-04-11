#FROM python:3.10.10-slim
FROM python:3.11-slim

#WORKDIR /app
WORKDIR /application


# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

