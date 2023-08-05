# py-redis-cachetools
cachetools core + redis

Requirements:
-------------
redis 3.5.3


Installation:
-------------

    pip install py-redis-cachetools

env variables:
-------------
    REDIS_HOST
    REDIS_DB


Usage:
------

    import time
    import cachetools, cachetools.rcache


    # cache = cachetools.rcache.RedisCache(ttl=60)

    cache = cachetools.rcache.PrefixedRedisCache("hb-cachetools-cache", ttl=60)


    @cachetools.cached(cache=cache)
    def test(a, b):
        return {
            'hi': 'hello'
        }



    a = 1
    while True:
        print(test(a, 2))
        print(a)
        time.sleep(1)
        a = a+1