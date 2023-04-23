# sample 1 - FastAPI

Env : Windows 11, VSCode, Python 3.9

## requirements

```txt
fastpi
celery
gevent
```

## run

Start Docker Redis, rabbitmq 

```bash
# docker compose up -d
docker-compose up -d
```

Run python script by this order

```bash
# 1. start celery worker
python -m celery -A app worker --pool=gevent  --concurrency=3 -l INFO
```

```bash
# 2. start FastAPI 
python -m uvicorn main:app --reload
```

```bash
# run test.py
python .\test.py
```

## 1. using 3 threads : --concurrency=3 

testing with test.py

### Before changing thread number (default 9)

```bash
{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
... (6 more results)
{'state': 'SUCCESS', 'result': 30}
cost : 3.472
```

### After changing thread number (9 -> 12)

```py
# test.py
...

if __name__ == "__main__":
    start = time.time()
    ww = [Worker(x) for x in range(12)] # <<<< change here

    [x.start() for x in ww]
    [x.join() for x in ww]
    print(f"cost : {time.time() - start:.3f}")
```

### test.py result

```bash
{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
...
{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
cost : 4.794
```

## 2. using 10 threads : --concurrency=10

### Before changing thread number (default 9)

```bash
{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
... (6 more results)
{'state': 'SUCCESS', 'result': 30}
cost : 1.521
```

### After changing thread number (9 -> 12)

```bash
{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
...
{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
cost : 2.746
```