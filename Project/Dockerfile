# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR .
COPY . .
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]