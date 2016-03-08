#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5

@author: wangyi
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime
def nj(currToday):
    db = Mysql.getConn()
    # today='20150522'
    try:
        cursor = db.cursor()
        sql = '''
            SELECT max(NEXTJYRQ) as JYRQ FROM NEXTJYRQ limit 1;
            '''
    #   print sql
    #   sql = sql.encode("utf8")
        cursor.execute(sql)
        row = cursor.fetchone()
        privdate = row["JYRQ"]
        cursor2 = db.cursor()
        sql2  = ''' INSERT NEXTJYRQ  VALUES('%s','%s'); ''' % (privdate,currToday)
        cursor2.execute(sql2)
        cursor2.close()
        db.commit()
    except Exception,e:
        print '获取样本数据查询错误'
        print e
    db.commit()
    db.close()