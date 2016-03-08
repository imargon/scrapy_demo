#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5
初始化所有的表数据到内存表中
@author: wangyi
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime


def di():
    db = Mysql.getConn()
    try:
        cursor = db.cursor()
        sql = '''
             delete from fscjmxhz_mem;
             insert fscjmxhz_mem select * from fscjmxhz;
            '''
    #   print sql
    #   sql = sql.encode("utf8")
        cursor.execute(sql)
        cursor.close()
        db.commit()
        cursor2 = db.cursor()
        sql2  = ''' delete from gl_mem; 
        insert gl_mem select * from gl; '''
        cursor2.execute(sql2)
        cursor2.close()
        db.commit()
    #     sql3 = '''
    #         insert lsgl_mem select * from lsgl;
    #     ''' 
    #     cursor3 = db.cursor()
    #     cursor3.execute(sql3)
    #     cursor3.close()
    #     db.commit()
    #     sql4 = '''
    #     insert sdqs_mem select * from sdqs;
    #     ''' 
    #     cursor4 = db.cursor()
    #     cursor4.execute(sql4)
    #     cursor4.close()
    #     db.commit()
        
    except Exception,e:
        print '初始化内存表出现错误'
        print e
    db.commit()
    db.close()

'''
Created on 2015-4-5
初始化所有的表数据到内存表中
@author: wangyi
'''
if __name__ == '__main__':
    di()