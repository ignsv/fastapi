FROM python:3.12.8

WORKDIR /app

COPY ./app .
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

