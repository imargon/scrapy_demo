#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5
大盘行业分析
@author: wangyi
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime
db = Mysql.getConn()
# today = datetime.strftime(datetime.now(),'%Y%m%d')
# today='20150522'
def dh(currTodya):
    try:
        cursor = db.cursor()
        sql = '''
            INSERT DP_FX
    SELECT JYRQ,AVG(PJJBZ) AS PJJBZ,AVG(PJLBZ) AS PJLBZ,AVG(ZFZ) AS ZFZ, AVG(NB) AS NB,
    AVG(HSL) AS HSL,SUM(JLR) AS JLR, SUM(CJL) AS CJL,SUM(CJE) AS CJE
    FROM FSCJMXHZ_MEM WHERE JYRQ='%s'
    GROUP BY JYRQ ;
            ''' % currTodya
    #   print sql
    #   sql = sql.encode("utf8")
        cursor.execute(sql)
        cursor.close()
        db.commit()
        cursor2 = db.cursor()
        sql2  = ''' INSERT HY_FX
    SELECT HY,JYRQ,AVG(PJJBZ) AS PJJBZ,AVG(PJLBZ) AS PJLBZ,AVG(ZFZ) AS ZFZ,AVG(NB) AS NB, AVG(HSL) AS HSL,SUM(JLR) AS JLR,SUM(CJL) AS CJL,SUM(CJE) AS CJE
    FROM
    (
    SELECT B.HY,A.JYRQ,A.PJJBZ,A.PJLBZ,A.ZFZ,A.NB,A.HSL,A.JLR,A.CJL,A.CJE
    FROM FSCJMXHZ_MEM AS A INNER JOIN  HY AS B  ON A.DM= B.DM
    WHERE A.JYRQ='%s'
    ) AS C
    GROUP BY HY,JYRQ ; ''' % currTodya
        cursor2.execute(sql2)
        cursor2.close()
        db.commit()
    except Exception,e:
        print '获取样本数据查询错误'
        print e
    db.commit()
    db.close()
