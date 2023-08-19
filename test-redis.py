# step 1: import the redis-py client package
import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information

from config_redis import REDIS_PROTOCOL, REDIS_HOST, REDIS_PORT

# redis_host = "localhost"
# redis_port = 6379
# redis_password = ""


def hello_redis():
    """Example Hello Redis Program"""

    # step 3: create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        redConn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

        hello_message = "yuhuuu Hello Redis!!!"
        print(f"sending message to redis '{hello_message}'")

        # step 4: Set the hello message in Redis
        redConn.set("msg:hello", hello_message)

        # step 5: Retrieve the hello message from Redis
        msg = redConn.get("msg:hello")
        print(f"retrieving message from redis '{msg}'")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()
