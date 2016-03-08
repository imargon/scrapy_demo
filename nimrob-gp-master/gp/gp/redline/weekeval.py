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
kvalue = 3
def selectALL():
        db = Mysql.getConn()
        rdl = 0;
        try:
            cursor = db.cursor()
            sql = '''
               select count(nzfz) ts
               FROM WEEK_FX;
                ''' 
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
               SELECT * FROM WEEK_FX;
                ''' 
#             print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["PJJBZ"])
                reMat[index,1] = float(row["PJLBZ"])
                reMat[index,2] = float(row["ZFZ"])
                reMat[index,3] = float(row["EPJ"])
                reMat[index,4] = float(row["LPJ"])
                reMat[index,5] = float(row["TPJ"])
                reMat[index,6] = float(row["MBS"])
                reMat[index,7] = float(row["MUDS"])
                reMat[index,8] = float(row["HSL"])
                reMat[index,9] = float(row["NB"])
                reMat[index,10] = float(row["JLR"])
                reLables.append(row["NZFZ"])
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

def selectTopTest(jyrq,jyrq2,jyrq3,jyrq4,rdl):
        db = Mysql.getConn()
        reMat = zeros((rdl,11))
        reLables = []
        dmLables = []
        index = 0

        try:
            cursor = db.cursor()
            sql = '''
                SELECT A.*,0 AS NZFZ FROM 
(
SELECT DM,AVG(PJJBZ) AS PJJBZ,AVG(PJLBZ) AS PJLBZ,AVG(ZFZ/10) AS ZFZ,AVG(NB) AS NB,AVG(HSL) AS HSL,
AVG(JLR/CJE * 10) AS JLR,AVG(upepj/downepj) AS EPJ, AVG(uplpj/downlpj) AS LPJ ,AVG(uptpj/downtpj) AS TPJ,AVG(mbs/mss) AS MBS, AVG(mups/mdowns) AS MUDS
FROM FSCJMXHZ_MEM
WHERE JYRQ >= '%s' AND JYRQ <= '%s'
GROUP BY DM
) AS A; 
                ''' % (jyrq,jyrq2)
    #                 print sql
    #             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["PJJBZ"])
                reMat[index,1] = float(row["PJLBZ"])
                reMat[index,2] = float(row["ZFZ"])
                reMat[index,3] = float(row["EPJ"])
                reMat[index,4] = float(row["LPJ"])
                reMat[index,5] = float(row["TPJ"])
                reMat[index,6] = float(row["MBS"])
                reMat[index,7] = float(row["MUDS"])
                reMat[index,8] = float(row["HSL"])
                reMat[index,9] = float(row["NB"])
                reMat[index,10] = float(row["JLR"])
                dmLables.append(row['DM'])
                reLables.append(row["NZFZ"])
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
    sortedDistIndicies = distances.argsort()
    classCount = {}
    classObj = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        if not classObj.has_key(voteIlabel):
            classObj[voteIlabel]= []
        classObj[voteIlabel].append(reobjs[sortedDistIndicies[i]])
#     print classCount
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
#     print sortedClassCount[0][0]
    return sortedClassCount[0][0]
def classifyTest(jyrq1,jyrq2,jyrq3,jyrq4):
    '''
    ybsd  : 样本开始日期   ybed：样本结束日期，csd:测试数据日期 my: 我的个股清单
    '''
    g,l,r = selectALL()
    tg,tl,tdm = selectTopTest(jyrq1,jyrq2,jyrq3,jyrq4,3000)
    zj = 0
    for i in range(0,len(tg[...,0])):
        cstl= classify1(tg[i,...],g,l,r,kvalue)
        db = Mysql.getConn()
        cursor = db.cursor()
        sql = '''
           INSERT WEEK_FX_JG VALUES('%s',%s);
            ''' % (tdm[zj],cstl)
#                 print sql
#             sql = sql.encode("utf8")
        cursor.execute(sql)
        cursor.close()
        db.commit()
        zj = zj + 1
if __name__ == '__main__':
#     curr = datetime.strftime(datetime.now(),'%Y%m%d')    
#     curr = '20150415'
    classifyTest('20150420','20150424','20150420','20150424')
    '''
#     Created on 2015年3月27日
#     每日历史结构评估
#     @author: nimrob
#     '''
#     db = Mysql.getConn()
#     try:
#         cursor = db.cursor()
#         sql = '''
#             SELECT JYRQ FROM NEXTJYRQ;
#             '''
#     #   print sql
#     #   sql = sql.encode("utf8")
#         cursor.execute(sql)
#         row = cursor.fetchone()
#         while row is not None:
#             csmbdate = row["JYRQ"]
#             classifyTest('20150106','20150423',csmbdate,[])
#             row = cursor.fetchone()
#         cursor.close()
#         db.commit()
#     except Exception,e:
#         print e
#     db.close()