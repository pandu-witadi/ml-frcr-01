#
import redis
#
from redis import ConnectionError
import logging

from config_redis import REDIS_PROTOCOL, REDIS_HOST, REDIS_PORT

logging.basicConfig()
logger = logging.getLogger(REDIS_PROTOCOL)

db = 0
rs = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=db)
try:
    rs.ping()
    print("ping success")
except ConnectionError:
    logger.error("redis not running")
    exit(0)
