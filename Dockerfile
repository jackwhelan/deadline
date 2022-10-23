FROM python:3.10.5-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=server.py
ENTRYPOINT [ "flask", "run" ]