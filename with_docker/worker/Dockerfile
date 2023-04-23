FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache

CMD python -m celery -A worker.worker worker --pool=gevent  --concurrency=10 -l INFO