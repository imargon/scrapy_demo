# -*- coding: utf-8 -*-  
import redis
from twisted.python import log
import MySQLdb
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
from json import JSONEncoder,JSONDecoder
import sys
import config
from datetime import datetime
import uuid


    
'''
数据库连接池
'''        
class Mysql(object):
#     args = (0,0,0,50,0,0,None)
#     conn_kwargs = {'host':config.databaseHost+':'+config.databasePort, 'user':config.databaseUserName, 'password':config.databaseUserPwd, 'database': config.databaseName,'charset':'utf8'}
#     __pool = PooledDB(pymssql, *args, **conn_kwargs)    
    __pool = PooledDB(creator=MySQLdb, mincached=config.mincached , maxcached=config.maxcached ,
                              host=config.dbhost , port=config.dbport , user=config.dbuser , passwd=config.dbpasswd ,
                              db=config.dbname,cursorclass=DictCursor,charset=config.charset)
    def __init__(self):
        pass
        
    @staticmethod
    def getConn():
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """        

        return Mysql.__pool.connection()

if __name__ == '__main__':
    #log.startLogging(sys.stdout)
    #print RedisDao().pop('ddd')
    #RedisDao().push('ddd', '我想我海')
    #RedisDao().pop('ddd')
    #print RedisDao().getdata('ccc')
    #print RedisDao().setdata('ccc', '我想我是海')
    #print RedisDao().getdata('ccc')
    #log1 = LogMsg()
    #log1.clientid = 1234
    #LogsqlDao.Log(log1)
    print Mysql.getConn()
    print Mysql.getConn()
    
