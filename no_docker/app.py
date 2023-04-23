from celery import Celery

app = Celery(
    "myapp",
    broker="amqp://admin:password@localhost:5672//",
    backend="redis://localhost:6379",
    task_acks_late=True,
)


@app.task(name="addTask")  # Named task
def add(x, y):
    return x + y
