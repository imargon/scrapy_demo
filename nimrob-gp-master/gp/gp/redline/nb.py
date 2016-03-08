#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5

@author: wangyi
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime



def updateDayNb(updateDate):
    db = Mysql.getConn()
    try:
        sql4 = '''
    SELECT JYRQ FROM NEXTJYRQ WHERE JYRQ < '%s' ORDER BY JYRQ DESC LIMIT 5;
    ''' % updateDate
        cursor4 = db.cursor()
        cursor4.execute(sql4)
        row4 = cursor4.fetchone()
        while row4 is not None:
            mindate = row4["JYRQ"]
            row4 = cursor4.fetchone()
        cursor4.close()
    
        sql3 = '''
        update fscjmxhz_mem as a,(select dm,avg(mcjl) as mcjl from fscjmxhz_mem  where jyrq >='%s' and jyrq < '%s' group by dm) as b set a.nb = a.mcjl/b.mcjl where a.dm=b.dm and a.jyrq='%s';
        ''' % (mindate,updateDate,updateDate)
        print sql3
        cursor3 = db.cursor()
        cursor3.execute(sql3)
        cursor3.close()
        db.commit()
    except Exception,e:
        print '更新指定日期的量比错误'
        print e
    db.commit()
    db.close()
    
def nnb(currToday):
    updateDayNb(currToday)
'''
 更新指定天的量比,[一般更新当前的量比数据]
'''
if __name__ == '__main__':
    today = datetime.strftime(datetime.now(),'%Y%m%d')
#     today='20150522'
    updateDayNb(today)