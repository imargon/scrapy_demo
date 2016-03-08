#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5

@author: wangyi
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime

def updatePrivGlNzfz(updateDate):
    db = Mysql.getConn()
    try:
        sql4 = '''
        UPDATE GL_MEM AS A,(SELECT DM,JYRQ,ZFZ,NZFZ FROM FSCJMXHZ_MEM WHERE JYRQ='%s') AS B SET A.ZFZ = B.ZFZ,A.NZFZ = B.NZFZ WHERE A.JYRQ=B.JYRQ AND A.DM=B.DM AND A.JYRQ='%s';
        ''' % (updateDate,updateDate)
        print sql4
        cursor4 = db.cursor()
        cursor4.execute(sql4)
        cursor4.close()
        db.commit()

    except Exception,e:
        print '更新概率前一日涨幅数据错误'
        print e
    db.commit()
    db.close()
def gz(privToday):
    updatePrivGlNzfz(privToday)    
'''
更新概率指定天的下一日涨幅，通常更新上个交易日的【下一日涨幅】 
'''
if __name__ == '__main__':
#     today = datetime.strftime(datetime.now(),'%Y%m%d')
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
#     privdate = '20150521'
    updatePrivGlNzfz(privdate)
    cursor.close()
    db.close()