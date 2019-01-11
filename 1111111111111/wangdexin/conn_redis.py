#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import redis

class RedisClient(object):
    def __init__(self):
        self._db = redis.Redis(host='127.0.0.1', port=6379, db=0)
        # 使用连接池连接数据库。这样就可以实现多个Redis实例共享一个连接池
        # pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
        # self._db = redis.Redis(connection_pool=pool)

    def get(self, key, value):
        try:
            self._db.set(key, value)
        except:
            return '插入失败'

    def pop(self, key, value):
        try:
            self._db.hdel(key, value)
        except:
            return '插入失败'
    def get_val(self, key):
        try:
            print ('*****************')
            return self._db.get(key)
        except:
            return '插入失败'