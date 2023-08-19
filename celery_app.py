#
#
from celery import Celery
from conf.conf_redis import REDIS_BROKER_URL, REDIS_RESULT_BACKEND


celery_app = Celery(
    "celery",
    backend=REDIS_BROKER_URL,
    broker=REDIS_RESULT_BACKEND
)
