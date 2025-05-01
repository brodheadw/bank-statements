from celery import Celery

celery_app = Celery(
    "bank_statements",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery_app.conf.task_routes = {"workers.tasks.*": {"queue": "default"}}