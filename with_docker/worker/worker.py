from time import sleep, time

from celery import Celery
from celery.app.task import Task

app = Celery(
    "myapp",
    broker="amqp://admin:password@rabbitmq:5672//",
    backend="redis://redis:6379",
    task_acks_late=True,
)


@app.task(name="addTask")  # Named task
def add(x, y):
    sleep(1)
    return x + y
