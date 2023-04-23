FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache

CMD python -m uvicorn app.main:app --host=0.0.0.0
