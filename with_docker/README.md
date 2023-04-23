# with docker example (using threads)

Env : Windows 11, VSCode, Python 3.9

## run

Start Docker Redis, rabbitmq, app, worker

```bash
# docker compose up -d
docker-compose up -d
```

## 0. change worker config

change files in [worker directory](./worker) and rebuild docker images

```bash
# after changing worker
docker-compose up -d --build
```

## 1. Testing with mock clients  

testing with test.py

### Before changing thread number (default 20)

```bash
python ./test.py

...

{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
... (17 more results)
{'state': 'SUCCESS', 'result': 30}
cost : 2.238
```

### After changing thread number (20 -> 30)

```bash
python ./test.py

...

{'state': 'SUCCESS', 'result': 30}
{'state': 'SUCCESS', 'result': 30}
... (27 more results)
{'state': 'SUCCESS', 'result': 30}
cost : 3.295
```