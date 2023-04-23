from time import sleep, time

from celery import Celery
from celery.app.task import Task

app = Celery(
    "myapp",
    broker="amqp://admin:password@localhost:5672//",
    backend="redis://localhost:6379",
    task_acks_late=True,
)


@app.task
def add(x, y):
    start = time()
    sleep(1)
    return x + y


if __name__ == "__main__":
    app.start()
