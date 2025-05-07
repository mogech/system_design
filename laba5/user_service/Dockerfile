FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-jose passlib[bcrypt] redis
EXPOSE 8000
CMD python init_db.py && uvicorn main:app --host 0.0.0.0 --port 8000
