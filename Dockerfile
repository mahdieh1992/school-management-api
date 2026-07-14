# pull official base imageF
FROM python:3.12.3-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# install dependencies
COPY . /app
RUN pip install --user -r requirements.txt

