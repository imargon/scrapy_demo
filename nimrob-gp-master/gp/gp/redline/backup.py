#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5
每日备份内存表数据回写表中
@author: wangyi
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime


def backupTodayData(updateDate):
    db = Mysql.getConn()
    try:
        cursor = db.cursor()
        sql = '''
        delete from fscjmxhz where jyrq >= '%s'; 
        insert fscjmxhz select * from fscjmxhz_mem where jyrq >='%s';
            ''' % (updateDate,updateDate)
        print sql
    #   sql = sql.encode("utf8")
        cursor.execute(sql)
        cursor.close()
        db.commit()
        print sql
        cursor2 = db.cursor()
        sql2  = '''
        delete from gl where jyrq >= '%s';
        insert gl select * from gl_mem where jyrq >= '%s'; 
        ''' % (updateDate,updateDate)
        cursor2.execute(sql2)
        cursor2.close()
        db.commit()
        print sql2
    except Exception,e:
        print '内存表回写备份错误'
        print e
        db.rollback()
    db.close()

def bkd(privToday):
    print privToday
    backupTodayData(privToday)
'''
Created on 2015-4-5
每日内存表数据回写表中
@author: wangyi
'''
    
'''
更新硬盘表中最近2天的数据，先删除硬盘表中2天数据，然后用内存表中的数据，回写硬盘表
【日期为上一个交易日】 
'''
if __name__ == '__main__':
    db = Mysql.getConn()
    cursor = db.cursor()
    sql = '''
        SELECT max(JYRQ) as JYRQ FROM NEXTJYRQ limit 1;
        '''
#   print sql
#   sql = sql.encode("utf8")
    cursor.execute(sql)
    row = cursor.fetchone()
    privdate = row["JYRQ"]
#     privdate = '20150522'
    backupTodayData(privdate)
    cursor.close()
