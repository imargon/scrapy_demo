#-*-coding:UTF-8-*-#
'''
Created on 2015年3月27日
实时流速预测
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


def selectALL(jyrq,jyrq2,mm):
        db = Mysql.getConn()
        rdl = 0
        jdm = []
        jrq = []
        try:
            cursor = db.cursor()
            sql = '''
               SELECT JYRQ,DM FROM SDQS 
               WHERE JYRQ >= '%s'  AND JYRQ <= '%s'
               GROUP BY JYRQ,DM
              HAVING COUNT(DM) >= 237
                ''' % (jyrq,jyrq2)
#                 print sql
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
        reMat = zeros((len(jdm),(mm-2)*1))
        reLables = []
        reObjs = []
        index = 0
        mindex = 0
        try:
            cursor = db.cursor()
            sql = '''
               SELECT A.DM,A.JYRQ,A.MNUM,IFNULL(A.PMBL/A.PMSL,0.0) AS LBZ,IFNULL(A.PMBS/A.PMSS,0.0) AS SBZ,A.PMH,A.PBH/(A.SP-A.PBH) * 10.0 AS ZF,FLOOR(A.PBH/(A.SP-A.PBH) * 100) AS ZFZ

FROM SDQS  AS A INNER JOIN
(
SELECT JYRQ,DM FROM SDQS 
           WHERE JYRQ >= '%s'  AND JYRQ <= '%s'
           GROUP BY JYRQ,DM
          HAVING COUNT(DM) >= 237
)  AS B 
ON A.DM = B.DM AND A.JYRQ = B.JYRQ

WHERE A.JYRQ >= '%s'  AND A.JYRQ <= '%s' AND A.MNUM != 1 AND (A.MNUM < %s OR A.MNUM=237)   ORDER BY DM,JYRQ,MNUM ASC;
                ''' % (jyrq,jyrq2,jyrq,jyrq2,mm)
#             print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                if row["MNUM"] !=237:
#                     reMat[index,mindex] = float(row["LBZ"])
#                     reMat[index,mindex + 1] = float(row["SBZ"])
#                     reMat[index,mindex + 2] = float(row["PMH"])
#                     reMat[index,mindex + 3] = float(row["ZF"])
                    reMat[index,mindex] = float(row["PMH"])
                    mindex = mindex + 1
                else:
                    mindex = 0
                    index = index + 1
                    reLables.append(row["ZFZ"])
                    reObjs.append('%s_%s' % (row["DM"],datetime.strftime(row['JYRQ'],'%Y-%m-%d')))
                row = cursor.fetchone()
            cursor.close()
        except Exception,e:
            print '组装样本数据错误'
            print e
        db.close()
        reMat = reMat[0:len(reLables),...]
        return reMat,reLables,reObjs

def selectYBTEST(jyrq,jyrq2,mm):
        db = Mysql.getConn()
        rdl = 0
        jdm = []
        jrq = []
        try:
            cursor = db.cursor()
            sql = '''
               SELECT JYRQ,DM FROM SDQS_MEM 
               WHERE JYRQ >= '%s'  AND JYRQ <= '%s'
               GROUP BY JYRQ,DM
              HAVING COUNT(DM) >= %s 
                ''' % (jyrq,jyrq2,mm)
#                 print sql
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
        reMat = zeros((len(jdm),(mm-2)*1))
        reLables = []
        reObjs = []
        index = 0
        mindex = 0
        try:
            cursor = db.cursor()
            sql = '''
               SELECT A.DM,A.JYRQ,A.MNUM,IFNULL(A.PMBL/A.PMSL,0.0) AS LBZ,IFNULL(A.PMBS/A.PMSS,0.0) AS SBZ,A.PMH,A.PBH/(A.SP-A.PBH) * 10.0 AS ZF,ROUND(A.PBH/(A.SP-A.PBH) * 100,2) AS ZFZ

FROM SDQS_MEM  AS A INNER JOIN
(
SELECT JYRQ,DM FROM SDQS_MEM 
           WHERE JYRQ >= '%s'  AND JYRQ <= '%s'
           GROUP BY JYRQ,DM
          HAVING COUNT(DM) >= %s 
)  AS B 
ON A.DM = B.DM AND A.JYRQ = B.JYRQ

WHERE A.JYRQ >= '%s'  AND A.JYRQ <= '%s' AND A.MNUM != 1 AND (A.MNUM < %s OR A.MNUM=237)   ORDER BY DM,JYRQ,MNUM ASC;
                ''' % (jyrq,jyrq2,mm,jyrq,jyrq2,mm)
            print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
#                 if row["MNUM"] !=237:
# #                     reMat[index,mindex] = float(row["LBZ"])
# #                     reMat[index,mindex + 1] = float(row["SBZ"])
# #                     reMat[index,mindex + 2] = float(row["PMH"])
# #                     reMat[index,mindex + 3] = float(row["ZF"])
#                     reMat[index,mindex] = float(row["PMH"])
#                     mindex = mindex + 1
#                 else:
#                     mindex = 0
#                     index = index + 1
#                     reLables.append(row["ZFZ"])
#                     reObjs.append(row["DM"])
                if row["MNUM"] !=237:
#                     print row["MNUM"]
#                     reMat[0,mindex] = float(row["LBZ"])
#                     reMat[0,mindex + 1] = float(row["SBZ"])
#                     reMat[0,mindex + 2] = float(row["PMH"])
#                     reMat[0,mindex + 3] = float(row["ZF"])
                    reMat[index,mindex] = float(row["PMH"])
                    mindex = mindex + 1
                if (mm-2)*1 == mindex:
                    reLables.append(row["ZFZ"])
                    reObjs.append('%s_%s' % (row["DM"],datetime.strftime(row['JYRQ'],'%Y-%m-%d')))
                    mindex = 0
                    index = index + 1
                
                row = cursor.fetchone()
            cursor.close()
        except Exception,e:
            print '组装样本数据错误'
            print e
        db.close()
        reMat = reMat[0:len(reLables),...]
        return reMat,reLables,reObjs
 
def selectDMTEST(jyrq,dm,mm):
        db = Mysql.getConn()
        reMat = zeros((1,(mm-2)*1))
        reLables = []
        reObjs = []
        mindex = 0
        try:
            cursor = db.cursor()
            sql = '''
               SELECT A.DM,A.JYRQ,A.MNUM,IFNULL(A.PMBL/A.PMSL,0.0) AS LBZ,IFNULL(A.PMBS/A.PMSS,0.0) AS SBZ,A.PMH,A.PBH/(A.SP-A.PBH) * 10.0 AS ZF,ROUND(A.PBH/(A.SP-A.PBH) * 100,2) AS ZFZ
FROM SDQS_MEM  AS A 
WHERE A.JYRQ = '%s'   AND A.DM='%s'  AND  A.MNUM != 1 AND (A.MNUM < %s OR A.MNUM=237)   ORDER BY DM,JYRQ,MNUM ASC;
                ''' % (jyrq,dm,mm)
            print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                if row["MNUM"] !=237:
                    print row["MNUM"]
#                     reMat[0,mindex] = float(row["LBZ"])
#                     reMat[0,mindex + 1] = float(row["SBZ"])
#                     reMat[0,mindex + 2] = float(row["PMH"])
#                     reMat[0,mindex + 3] = float(row["ZF"])
                    reMat[0,mindex] = float(row["PMH"])
                if (mm-3)*1 == mindex:
                    reLables.append(row["ZFZ"])
                    reObjs.append('%s_%s' % (row["DM"],datetime.strftime(row['JYRQ'],'%Y-%m-%d')))
                mindex = mindex + 1
                row = cursor.fetchone()
            cursor.close()
        except Exception,e:
            print '组装样本数据错误'
            print e
        db.close()
#         reMat = reMat[0:len(reLables),...]
        return reMat,reLables,reObjs

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
    return sortedClassCount[0][0],classObj[sortedClassCount[0][0]]
def classifyTest(sd,ed,cd,dm,mm):
#     g,l,dm = selectTop('20150330',500)
#     g,l = selectAVG('20150105','20150330')
    g,l,r = selectALL(sd,ed,mm)
    sdate = cd
#     tg,tl,tdm = selectYBTEST(sdate, sdate,190)
    
    tg,tl,tdm = selectDMTEST(sdate,dm,mm)
#     print tl
#     cstl,reobj = classify1(tg[...,0],g,l,r,100)
#     print 'cstl:', cstl
    error = 0
    zj = 0
    mbz = []
    mymbz = []
    for i in range(0,len(tg[...,0])):
        cstl,reobj = classify1(tg[i,...],g,l,r,99)
        zcs = float(len(reobj))
        try:
            sjz = tl[zj]
        except Exception,e:
            sjz = 0
#         if cstl >= 5 and cstl <= 11:
        mbz.append([tdm[zj],cstl,sjz])
        if cstl <= sjz:
            print u'%s:事实:%s   评估:%s   ok'  % (tdm[zj],sjz,cstl)
        else:
            print u'%s:事实:%s   评估:%s   error'  % (tdm[zj],sjz,cstl)
            error = error + 1
        db = Mysql.getConn()
        cursor = db.cursor()
        sql = '''
           delete from lsgl_mem where  dm='%s' and jyrq = '%s';
            ''' % (tdm[zj],sdate)
#                 print sql
#             sql = sql.encode("utf8")
        cursor.execute(sql)
        cursor.close()
        db.commit()
        gl = {"P00":0,"P01":0,"P02":0,"P03":0,"P04":0,"P05":0,"P06":0,"P07":0,"P08":0,"P09":0,"P010":0,"P10":0,"P20":0,"P30":0,"P40":0,"P50":0,"P60":0,"P70":0,"P80":0,"P90":0,"P100":0}
        zfzh = 0.0
        zfzcs = 0.0
        sjz = 0.0
        for o in reobj:
            try:
                csdmrq = o.split('_')
                cursor = db.cursor()
                sql = '''
                   select zfz from fscjmxhz_mem where  dm='%s' and jyrq > '%s'
order by jyrq asc limit 3;
                    ''' % (csdmrq[0],csdmrq[1])
#                 print sql
    #             sql = sql.encode("utf8")
                cursor.execute(sql)
                row = cursor.fetchone()
                while row is not None:
                    if row['zfz'] == 0:
                        gl["P00"] = gl.get("P00",0) + 1
                    elif row["zfz"] >= -1 and row["zfz"] < 0:
                        gl["P01"] = gl.get("P01",0) + 1
                    elif row["zfz"] >= -2 and row["zfz"] < -1:
                        gl["P02"] = gl.get("P02",0) + 1
                    elif row["zfz"] >= -3 and row["zfz"] < -2:
                        gl["P03"] = gl.get("P03",0) + 1
                    elif row["zfz"] >= -4 and row["zfz"] < -3:
                        gl["P04"] = gl.get("P04",0) + 1
                    elif row["zfz"] >= -5 and row["zfz"] < -4:
                        gl["P05"] = gl.get("P05",0) + 1
                    elif row["zfz"] >= -6 and row["zfz"] < -5:
                        gl["P06"] = gl.get("P06",0) + 1
                    elif row["zfz"] >= -7 and row["zfz"] < -6:
                        gl["P07"] = gl.get("P07",0) + 1
                    elif row["zfz"] >= -8 and row["zfz"] < -7:
                        gl["P08"] = gl.get("P08",0) + 1
                    elif row["zfz"] >= -9 and row["zfz"] < -8:
                        gl["P09"] = gl.get("P09",0) + 1
                    elif row["zfz"] < -9:
                        gl["P010"] = gl.get("P010",0) + 1
                    elif row["zfz"] <=1  and row["zfz"] > 0:
                        gl["P10"] = gl.get("P10",0) + 1
                    elif row["zfz"] <=2  and row["zfz"] > 1:
                        gl["P20"] = gl.get("P20",0) + 1
                    elif row["zfz"] <= 3 and row["zfz"] > 2:
                        gl["P30"] = gl.get("P30",0) + 1
                    elif row["zfz"] <= 4 and row["zfz"] > 3:
                        gl["P40"] = gl.get("P40",0) + 1
                    elif row["zfz"] <= 5 and row["zfz"] > 4:
                        gl["P50"] = gl.get("P50",0) + 1
                    elif row["zfz"] <= 6 and row["zfz"] > 5:
                        gl["P60"] = gl.get("P60",0) + 1
                    elif row["zfz"] <= 7 and row["zfz"] > 6:
                        gl["P70"] = gl.get("P70",0) + 1
                    elif row["zfz"] <= 8 and row["zfz"] > 7:
                        gl["P80"] = gl.get("P80",0) + 1
                    elif row["zfz"] <= 9 and row["zfz"] > 8:
                        gl["P90"] = gl.get("P90",0) + 1
                    elif row["zfz"] > 9:
                        gl["P110"] = gl.get("P110",0) + 1
                    zfzcs = zfzcs + 1.0
                    zfzh = zfzh + row["zfz"]
                    row = cursor.fetchone()
                cursor.close()
 
            except Exception,e:
                print '数据查询错误'
                print e
        try:
            csdmrq = o.split('_')
            cursor = db.cursor()
            sql = '''
               INSERT LSGL_MEM(DM,
JYRQ ,
P00 ,
P01 ,
P02 ,
P03 ,
P04 ,
P05 ,
P06 ,
P07 ,
P08 ,
P09 ,
P010 ,
P10 ,
P20 ,
P30 ,
P40 ,
P50 ,
P60 ,
P70 ,
P80 ,
P90 ,
P100,MB) VALUES('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                ''' % (tdm[zj],sdate,gl["P00"]/zfzcs,gl["P01"]/zfzcs,gl["P02"]/zfzcs,gl["P03"]/zfzcs,gl["P04"]/zfzcs,gl["P05"]/zfzcs,gl["P06"]/zfzcs,gl["P07"]/zfzcs,gl["P08"]/zfzcs,gl["P09"]/zfzcs,gl["P010"]/zfzcs,gl["P10"]/zfzcs,gl["P20"]/zfzcs,gl["P30"]/zfzcs,gl["P40"]/zfzcs,gl["P50"]/zfzcs,gl["P60"]/zfzcs,gl["P70"]/zfzcs,gl["P80"]/zfzcs,gl["P90"]/zfzcs,gl["P100"]/zfzcs,zfzh/zfzcs)
#                 print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            cursor.close()
            db.commit()
        except Exception,e:
            print '数据查询错误'
            print e
#         if tdm[zj] in my:
#             mymbz.append([tdm[zj],cstl,sjz])
    zj = zj + 1
    print '代码   | 评估涨幅 | 实际涨幅\n' 
    for i in mbz:
        print '%s   |   %s   |   %s\n'  % (i[0],i[1],i[2])
    for i in mymbz:
        print '%s   |   %s   |   %s\n'  % (i[0],i[1],i[2])
    print "error rate:   %s"  % (error/float(len(mbz))) ,sdate
    
classifyTest('20150323','20150402','20150416','600512',200) 
