#-*-coding:UTF-8-*-#
'''
Created on 2015年3月27日
每日历史结构评估
@author: nimrob
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime
kvalue = 99
def selectALL(jyrq,jyrq2,currdate):
        db = Mysql.getConn()
        rdl = 0;
        try:
            cursor = db.cursor()
            sql = '''
               select count(jyrq) ts
               from fscjmxhz_mem
            where jyrq >= '%s'  and jyrq <  '%s' and jyrq !='%s' and dm like '%s' and nzfz > 9; 
                ''' % (jyrq,jyrq2,currdate,'002%')
            print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            rdl = row['ts']
            cursor.close()
        except Exception,e:
            print '数据查询错误1'
            print e
        reMat = zeros((rdl,11))
        reLables = []
        reObjs = []
        index = 0
        try:
            cursor = db.cursor()
            sql = '''
               select avg(d.pjjbz) as pjjbz,avg(d.pjlbz) as pjlbz,
               avg(floor(d.nzfz)) as nzfz,avg(d.zfz/10.0) as zfz,
               avg(d.upepj/d.downepj) as epj,avg(d.uplpj/d.downlpj) as lpj,avg(d.uptpj/d.downtpj) as tpj,
               avg(d.mbs/d.mss) as mbs,avg(d.mups/d.mdowns) as muds,avg(d.hsl * 10) as hsl,avg(d.nb) as nb,avg(d.jlr/d.cje * 10) as jlr
               from fscjmxhz_mem as d 
               where d.jyrq >= '%s'  and d.jyrq < '%s' and d.jyrq !='%s' and dm like '%s' and nzfz > 9; 
                ''' % (jyrq,jyrq2,currdate,'002%')
#             print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["pjjbz"])
                reMat[index,1] = float(row["pjlbz"])
                reMat[index,2] = float(row["zfz"])
                reMat[index,3] = float(row["epj"])
                reMat[index,4] = float(row["lpj"])
                reMat[index,5] = float(row["tpj"])
                reMat[index,6] = float(row["mbs"])
                reMat[index,7] = float(row["muds"])
                reMat[index,8] = float(row["hsl"])
                reMat[index,9] = float(row["nb"])
                reMat[index,10] = float(row["jlr"])
                reLables.append(row["nzfz"])
                reObjs.append('%s_%s' % ("dm","jyrq"))
                row = cursor.fetchone()
                index = index + 1
            cursor.close()
        except Exception,e:
            print '数据查询错误2'
            print e
        db.close()
        reMat = reMat[0:len(reLables),...]
        return reMat,reLables,reObjs

def selectTopTest(jyrq,rdl):
        db = Mysql.getConn()
        reMat = zeros((rdl,11))
        reLables = []
        dmLables = []
        index = 0

        try:
            cursor = db.cursor()
            sql = '''
                select a.dm,a.pjjbz,a.pjlbz,
                floor(a.nzfz) as nzfz,a.zfz/10.0 as zfz,
               a.upepj/a.downepj as epj,a.uplpj/a.downlpj as lpj,a.uptpj/a.downtpj as tpj,
               a.mbs/a.mss as mbs,a.mups/a.mdowns as muds,a.hsl * 10 as hsl,a.nb,a.jlr/a.cje * 10 as jlr
               from fscjmxhz_mem as a 
               where a.jyrq = '%s' and a.dm like '%s';
                ''' % (jyrq,'002%')
    #                 print sql
    #             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["pjjbz"])
                reMat[index,1] = float(row["pjlbz"])
                reMat[index,2] = float(row["zfz"])
                reMat[index,3] = float(row["epj"])
                reMat[index,4] = float(row["lpj"])
                reMat[index,5] = float(row["tpj"])
                reMat[index,6] = float(row["mbs"])
                reMat[index,7] = float(row["muds"])
                reMat[index,8] = float(row["hsl"])
                reMat[index,9] = float(row["nb"])
                reMat[index,10] = float(row["jlr"])
                dmLables.append(row['dm'])
                reLables.append(row["nzfz"])
                row = cursor.fetchone()
                index = index + 1
            cursor.close()
        except Exception,e:
            print '获取样本数据查询错误'
            print e
        db.close()
        reMat = reMat[0:len(reLables),...]
        return reMat,reLables,dmLables

def classify1(inX,dataSet,labels,reobjs,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    return distances.sum(axis=0)
def classifyTest(ybsd,ybed,csd,my):
    '''
    ybsd  : 样本开始日期   ybed：样本结束日期，csd:测试数据日期 my: 我的个股清单
    '''
    g,l,r = selectALL(ybsd,ybed,csd)
    sdate = csd
    tg,tl,tdm = selectTopTest(sdate,3000)
    zj = 0
    for i in range(0,len(tg[...,0])):
        cstl= classify1(tg[i,...],g,l,r,kvalue)
        db = Mysql.getConn()
        cursor = db.cursor()
        sql = '''
           INSERT ZT_FX VALUES('%s','%s',%s);
            ''' % (tdm[zj],sdate,cstl)
#                 print sql
#             sql = sql.encode("utf8")
        cursor.execute(sql)
        cursor.close()
        db.commit()
        zj = zj + 1
if __name__ == '__main__':
#     curr = datetime.strftime(datetime.now(),'%Y%m%d')    
#     curr = '20150415'
#     classifyTest('20150106',curr,curr,[])
    '''
    Created on 2015年3月27日
    每日历史结构评估
    @author: nimrob
    '''
    db = Mysql.getConn()
    try:
        cursor = db.cursor()
        sql = '''
            SELECT JYRQ FROM NEXTJYRQ;
            '''
    #   print sql
    #   sql = sql.encode("utf8")
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            csmbdate = row["JYRQ"]
            classifyTest('20150106','20150423',csmbdate,[])
            row = cursor.fetchone()
        cursor.close()
        db.commit()
    except Exception,e:
        print e
    db.close()