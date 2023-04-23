from app import add
from celery.app.task import Task
from celery.result import AsyncResult
import uvicorn
from fastapi import FastAPI


BROKER = "amqp://admin:password@localhost:5672//"

add: Task
app = FastAPI(title="Example")


def on_raw_message(body):
    print(body)


@app.get("/")
async def calculate():
    a = add.apply_async(args=(10, 20))
    return a.task_id


@app.get("/task")
async def calculate(id: str):
    res: AsyncResult = add.AsyncResult(id, app=add)
    # https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery-result

    if res.state != "SUCCESS":
        return {"state": res.state, "result": None}

    return {"state": res.state, "result": res.get()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
