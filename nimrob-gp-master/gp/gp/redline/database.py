#-*-coding:UTF-8-*-#
'''
@author: wangyi
数据库链接，缓存链接
'''
import redis
import MySQLdb
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
import config
import pymongo
import amqp

# 
# class Mongo(object):
#     _pool = pymongo.connection.MongoClient(host=config.mongohost,port=config.mongoport,max_pool_size=config.max_pool_size,auto_start_request=config.auto_start_request)
#     def __init__(self):
#         #Mongo._pool[config.mongodb].authenticate(config.mongouser,config.mongopwd)
#         pass
#     @staticmethod
#     def getPool():
#         Mongo._pool[config.mongodb].authenticate(config.mongouser,config.mongopwd)        
#         return Mongo._pool[config.mongodb]

class MyRedis(object):
    __pool = redis.ConnectionPool(host=config.redis_ip, port=config.redis_port, db=config.redis_db,max_connections=config.redis_conns)
    def __init__(self):
        pass
    @staticmethod
    def getPool():
        return MyRedis.__pool
    
class Mongo(object):
    _pool = pymongo.connection.MongoClient(host=config.mongohost,port=config.mongoport,max_pool_size=config.max_pool_size,auto_start_request=config.auto_start_request)
    def __init__(self):
        #Mongo._pool[config.mongodb].authenticate(config.mongouser,config.mongopwd)
        pass
    @staticmethod
    def getPool():
        Mongo._pool[config.mongodb].authenticate(config.mongouser,config.mongopwd)
        return Mongo._pool[config.mongodb]

def exists(key):
    pool  = MyRedis.getPool()
    rd = redis.Redis(connection_pool=pool)
    return rd.exists(key)
def set(key,value):
    pool  = MyRedis.getPool()
    rd = redis.Redis(connection_pool=pool)
    rd.set(key, value)
    
def get(key):
    pool  = MyRedis.getPool()
    rd = redis.Redis(connection_pool=pool)
    return rd.get(key)  