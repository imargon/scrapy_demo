#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5

@author: wangyi
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime

def updatePrivDayNzfz(updateDate):
    db = Mysql.getConn()
    try:
        sql3 = '''
        update fscjmxhz_mem as a,fscjmxhz_mem as b,nextjyrq as c set a.nzfz = b.zfz where a.jyrq = c.jyrq and c.nextjyrq = b.jyrq and  a.dm = b.dm and a.jyrq='%s';
        ''' % updateDate
        print sql3
        cursor3 = db.cursor()
        cursor3.execute(sql3)
        cursor3.close()
        db.commit()
    except Exception,e:
        print '更新前一日，【下日涨幅】错误'
        print e
    db.commit()
    db.close()

def nf(privToday):
    updatePrivDayNzfz(privToday)
'''
更新指定天的下一日涨幅，通常更新上个交易日的【下一日涨幅】 
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
    updatePrivDayNzfz(privdate)
    cursor.close()
    db.close()
