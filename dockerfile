FROM python:3.10-alpine

RUN pip install fastapi uvicorn pymongo pydantic



WORKDIR /app


COPY /app/ . 

EXPOSE 8763

CMD sh -c 'python3 seeder.py && uvicorn api:app --host 127.0.0.1 --port 8763'

