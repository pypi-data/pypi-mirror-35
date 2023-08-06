
import redis


class RedisHelper():
    def __init__(self, host='localhost',db=0, port=6379):
        self.__redis = redis.StrictRedis(host, port,db)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
    def mget(self,keylist):
        return self.__redis.mget(keylist)

    def set(self, key, value,ex=None):
        self.__redis.set(key, value)
        if ex:
            self.__redis.expire(key,ex)

    def ttl(self,key):
        return self.__redis.ttl(key)

    def incr(self,key):
        return self.__redis.incr(key)
    def getKeys(self):
        return self.__redis.keys()

def is_json(res):
    import json
    try:
        json.loads(res)
    except:
        return False
    else:
        return True

