# python-celery-poc

python celery example using rabbitmq, redis, FastAPI, Docker

## 1. python command-line (no_docker)

Read [no docker example README.md](./no_docker/README.md)

## 2. with docker (and scaling)

Read [docker example README.md](./with_docker/README.md)

to scale workers, run 

```bash
docker-compose up --scale worker=3
```