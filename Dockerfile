FROM python:3.10

WORKDIR /stadions

ENV PYTHONSLIMBUSTER 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000



