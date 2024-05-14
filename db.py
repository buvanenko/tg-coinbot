import redis.asyncio as redis

import config

client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)
