#-*-coding:UTF-8-*-#
'''
Created on 2015年3月27日
对导入的流速数据进行转换，提供处理速度
@author: nimrob
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime

# 样本数据提供，jyrq:选择日期，rdl:选择20个档的每个挡的量
#使用指定日期的前一天的行为结构数据做为样本，通过修改rdl 来控制样本数据的大小，默认选择样本的时候使用随机每挡的RDL条
# def createDataSet(jyrq,rdl):
#     group,labels,tm = selectTop(jyrq,rdl)
#     return group,labels,tm


def selectALL(jyrq,jyrq2):
        db = Mysql.getConn()
        jdm = []
        jrq = []
        try:
            cursor = db.cursor()
            sql = '''
               SELECT JYRQ,DM FROM SDQS_MEM 
               WHERE JYRQ >= '%s'  AND JYRQ <= '%s'
               GROUP BY JYRQ,DM
              HAVING COUNT(DM) >= 237
                ''' % (jyrq,jyrq2)
#             print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                jdm.append(row["DM"])
                jrq.append(row["JYRQ"])
                row = cursor.fetchone()
            cursor.close()
        except Exception,e:
            print ' 获取记录集清单错误'
            print e
#         print len(jdm),len(jrq)
        for i in range(0,len(jdm)):
            zfz = 0.0
            nzfz = 0.0 
            v = []
            try:
                cursor3 = db.cursor()
                sql3 = u'''
                   SELECT A.DM,A.JYRQ,A.MNUM,A.PMH,B.ZFZ,B.DLSC AS NZFZ
    FROM SDQS_MEM  AS A INNER JOIN 
    (SELECT DM,JYRQ,ZFZ,DLSC FROM FSCJMXHZ_MEM WHERE JYRQ='%s' AND DM='%s') AS B
    ON A.DM= B.DM AND A.JYRQ=B.JYRQ
    
    WHERE A.JYRQ = '%s'  AND A.DM='%s'  AND A.MNUM > 2 AND A.MNUM < 236 ORDER BY A.DM,A.JYRQ,A.MNUM ASC;
                    ''' % (jrq[i],jdm[i],jrq[i],jdm[i])
#                 print sql3
    #             sql = sql.encode("utf8")
                cursor3.execute(sql3)
                row = cursor3.fetchone()
                while row is not None:
                    if row["MNUM"] % 5 == 0:
                        v.append(row["PMH"])
                    if row["MNUM"] == 235:
                        zfz = row["ZFZ"]
                        nzfz = row["NZFZ"]
                    row = cursor3.fetchone()
                cursor3.close()
            except Exception,e:
                print '组装样本数据错误'
                print e
            try:
#                 print v,zfz,nzfz
                sql2 = '''
                   INSERT LSDAY_MEM VALUES('%s','%s',
                   %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                   %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                   %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                   %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                   %s,%s,%s,%s,%s,%s,
                   %s,%s,%s);
                    ''' % (jdm[i],jrq[i],
                           v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13],v[14],v[15],v[16],v[17],v[18],v[19],v[20],v[21],v[22],v[23],v[24],v[25],v[26],v[27],v[28],v[29],v[30],v[31],v[32],v[33],v[34],v[35],v[36],v[37],v[38],v[39],v[40],v[41],v[42],v[43],v[44],v[45],v[46],
                           zfz,nzfz)
#                 print sql2
    #             sql = sql.encode("utf8")
                cursor2 = db.cursor()
                cursor2.execute(sql2)
                cursor2.close()
                db.commit()
            except Exception,e:
                print '数据查询错误'
                print e
            print jdm[i],jrq[i]
        db.close()
selectALL('20150303','20150403')

'''
Created on 2015年3月27日
对导入的流速数据进行转换，提供处理速度
@author: nimrob
'''