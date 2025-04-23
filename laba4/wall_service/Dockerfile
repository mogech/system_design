FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pymongo python-jose pydantic
EXPOSE 8001
CMD python init_db.py && uvicorn main:app --host 0.0.0.0 --port 8001
