#-*-coding:UTF-8-*-#
'''
Created on 2015年3月27日
流速流量模型  收盘后预测，前提已经转换好数据
@author: nimrob
'''
from numpy import  *
import operator
from redline.dbhelper import Mysql
from datetime import datetime

def selectALL(jyrq,jyrq2):
        db = Mysql.getConn()
        rdl = 0;
        try:
            cursor = db.cursor()
            sql = '''
               select count(jyrq) ts
               from lsday_mem
               where jyrq >= '%s'  and jyrq <=  '%s'; 
                ''' % (jyrq,jyrq2)
#                 print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            rdl = row['ts']
            cursor.close()
        except Exception,e:
            print '数据查询错误'
            print e
        reMat = zeros((rdl,48))
        reLables = []
        reObjs = []
        index = 0
        try:
            cursor = db.cursor()
            sql = '''
               select d.dm,d.jyrq,
                d.m2 ,d.m3 ,d.m4 ,d.m5 ,d.m6 ,d.m7 ,d.m8 ,d.m9 ,d.m10 ,d.m11 ,
                   d.m12 ,d.m13 ,d.m14 ,d.m15 ,d.m16 ,d.m17 ,d.m18 ,d.m19 ,d.m20 ,d.m21 ,
                   d.m22 ,d.m23 ,d.m24 ,d.m25 ,d.m26 ,d.m27 ,d.m28 ,d.m29 ,d.m30 ,d.m31 ,
                   d.m32 ,d.m33 ,d.m34 ,d.m35 ,d.m36 ,d.m37 ,d.m38 ,d.m39 ,d.m40 ,d.m41 ,
                   d.m42 ,d.m43 ,d.m44 ,d.m45 ,d.m46 ,d.m47 ,d.m48,
               floor(d.zfza) as zfz,d.zfz/100.0 as zfza
               from lsday_mem as d 
               where d.jyrq >= '%s'  and d.jyrq <= '%s'; 
                ''' % (jyrq,jyrq2)
#             print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["m2"])
                reMat[index,1] = float(row["m3"])
                reMat[index,2] = float(row["m4"])
                reMat[index,3] = float(row["m5"])
                reMat[index,4] = float(row["m6"])
                reMat[index,5] = float(row["m7"])
                reMat[index,6] = float(row["m8"])
                reMat[index,7] = float(row["m9"])
                reMat[index,8] = float(row["m10"])
                reMat[index,9] = float(row["m11"])
                reMat[index,10] = float(row["m12"])
                reMat[index,11] = float(row["m13"])
                reMat[index,12] = float(row["m14"])
                reMat[index,13] = float(row["m15"])
                reMat[index,14] = float(row["m16"])
                reMat[index,15] = float(row["m17"])
                reMat[index,16] = float(row["m18"])
                reMat[index,17] = float(row["m19"])
                reMat[index,18] = float(row["m20"])
                reMat[index,19] = float(row["m21"])
                reMat[index,20] = float(row["m22"])
                reMat[index,21] = float(row["m23"])
                reMat[index,22] = float(row["m24"])
                reMat[index,23] = float(row["m25"])
                reMat[index,24] = float(row["m26"])
                reMat[index,25] = float(row["m27"])
                reMat[index,26] = float(row["m28"])
                reMat[index,27] = float(row["m29"])
                reMat[index,28] = float(row["m30"])
                reMat[index,29] = float(row["m31"])
                reMat[index,30] = float(row["m32"])
                reMat[index,31] = float(row["m33"])
                reMat[index,32] = float(row["m34"])
                reMat[index,33] = float(row["m35"])
                reMat[index,34] = float(row["m36"])
                reMat[index,35] = float(row["m37"])
                reMat[index,36] = float(row["m38"])
                reMat[index,37] = float(row["m39"])
                reMat[index,38] = float(row["m40"])
                reMat[index,39] = float(row["m41"])
                reMat[index,40] = float(row["m42"])
                reMat[index,41] = float(row["m43"])
                reMat[index,42] = float(row["m44"])
                reMat[index,43] = float(row["m45"])
                reMat[index,44] = float(row["m46"])
                reMat[index,45] = float(row["m47"])
                reMat[index,46] = float(row["m48"])
                reMat[index,47] = float(row["zfza"])
                reLables.append(row["zfz"])
                reObjs.append('%s_%s' % (row["dm"],datetime.strftime(row['jyrq'],'%Y-%m-%d')))
                row = cursor.fetchone()
                index = index + 1
            cursor.close()
        except Exception,e:
            print '数据样本查询错误'
            print e
        db.close()
        reMat = reMat[0:len(reLables),...]
        return reMat,reLables,reObjs

def selectTopTest(jyrq):
        db = Mysql.getConn()
        reMat = zeros((3000,48))
        reLables = []
        dmLables = []
        index = 0

        try:
            cursor = db.cursor()
            sql = '''
               select d.dm,d.jyrq,
                d.m2 ,d.m3 ,d.m4 ,d.m5 ,d.m6 ,d.m7 ,d.m8 ,d.m9 ,d.m10 ,d.m11 ,
                   d.m12 ,d.m13 ,d.m14 ,d.m15 ,d.m16 ,d.m17 ,d.m18 ,d.m19 ,d.m20 ,d.m21 ,
                   d.m22 ,d.m23 ,d.m24 ,d.m25 ,d.m26 ,d.m27 ,d.m28 ,d.m29 ,d.m30 ,d.m31 ,
                   d.m32 ,d.m33 ,d.m34 ,d.m35 ,d.m36 ,d.m37 ,d.m38 ,d.m39 ,d.m40 ,d.m41 ,
                   d.m42 ,d.m43 ,d.m44 ,d.m45 ,d.m46 ,d.m47 ,d.m48,
               floor(d.zfza) as zfz,d.zfz/100.0 as zfza
               from lsday_mem as d 
               where d.jyrq = '%s'; 
                ''' % (jyrq)
    #                 print sql
    #             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["m2"])
                reMat[index,1] = float(row["m3"])
                reMat[index,2] = float(row["m4"])
                reMat[index,3] = float(row["m5"])
                reMat[index,4] = float(row["m6"])
                reMat[index,5] = float(row["m7"])
                reMat[index,6] = float(row["m8"])
                reMat[index,7] = float(row["m9"])
                reMat[index,8] = float(row["m10"])
                reMat[index,9] = float(row["m11"])
                reMat[index,10] = float(row["m12"])
                reMat[index,11] = float(row["m13"])
                reMat[index,12] = float(row["m14"])
                reMat[index,13] = float(row["m15"])
                reMat[index,14] = float(row["m16"])
                reMat[index,15] = float(row["m17"])
                reMat[index,16] = float(row["m18"])
                reMat[index,17] = float(row["m19"])
                reMat[index,18] = float(row["m20"])
                reMat[index,19] = float(row["m21"])
                reMat[index,20] = float(row["m22"])
                reMat[index,21] = float(row["m23"])
                reMat[index,22] = float(row["m24"])
                reMat[index,23] = float(row["m25"])
                reMat[index,24] = float(row["m26"])
                reMat[index,25] = float(row["m27"])
                reMat[index,26] = float(row["m28"])
                reMat[index,27] = float(row["m29"])
                reMat[index,28] = float(row["m30"])
                reMat[index,29] = float(row["m31"])
                reMat[index,30] = float(row["m32"])
                reMat[index,31] = float(row["m33"])
                reMat[index,32] = float(row["m34"])
                reMat[index,33] = float(row["m35"])
                reMat[index,34] = float(row["m36"])
                reMat[index,35] = float(row["m37"])
                reMat[index,36] = float(row["m38"])
                reMat[index,37] = float(row["m39"])
                reMat[index,38] = float(row["m40"])
                reMat[index,39] = float(row["m41"])
                reMat[index,40] = float(row["m42"])
                reMat[index,41] = float(row["m43"])
                reMat[index,42] = float(row["m44"])
                reMat[index,43] = float(row["m45"])
                reMat[index,44] = float(row["m46"])
                reMat[index,45] = float(row["m47"])
                reMat[index,46] = float(row["m48"])
                reMat[index,47] = float(row["zfza"])
                dmLables.append(row['dm'])
                reLables.append(row["zfz"])
                row = cursor.fetchone()
                index = index + 1
            cursor.close()
        except Exception,e:
            print '获取样本数据查询错误'
            print e
        db.close()
        reMat = reMat[0:len(reLables),...]
        return reMat,reLables,dmLables
 
def selectDmTest(jyrq,dm):
    db = Mysql.getConn()
    reMat = zeros((1,39))
    reLables = []
    dmLables = []
    index = 0
    try:
        cursor = db.cursor()
        sql = '''
            select a.dm,a.pjjbz,a.pjlbz,
           a.gjbdebz,a.gjbdlbz,a.gjbdfsbz,
           a.gjsdebz,a.gjsdlbz,a.gjsdfsbz,
           a.zjbdebz,a.zjbdlbz,a.zjbdfsbz,
           a.zjsdebz,a.zjsdlbz,a.zjsdfsbz,
           a.djbdebz,a.djbdlbz,a.djbdfsbz,
           a.djsdebz,a.djsdlbz,a.djsdfsbz,
           a.glbdebz,a.glbdlbz,a.glbdfsbz,
           a.glsdebz,a.glsdlbz,a.glsdfsbz,
           a.zlbdebz,a.zlbdlbz,a.zlbdfsbz,
           a.zlsdebz,a.zlsdlbz,a.zlsdfsbz,
           a.dlbdebz,a.dlbdlbz,a.dlbdfsbz,
           a.dlsdebz,a.dlsdlbz,a.dlsdfsbz,a.zfz,a.zfz/100.0 as zfza 
           from fscjmxhz_mem as a 
           left join ( 
            select dm,jyrq,zfz from fscjmxhz_mem 
            WHERE jyrq= (select jyrq from fscjmxhz_mem where jyrq > '%s' 
order by jyrq asc limit 1) 
            )
            as b 
           on a.dm = b.dm
            where a.jyrq = '%s' and a.dm = '%s';
            ''' % (jyrq,jyrq,dm)
#                 print sql
#             sql = sql.encode("utf8")
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            reMat[index,0] = float(row["pjjbz"])
            reMat[index,1] = float(row["pjlbz"])
            reMat[index,2] = float(row["gjbdebz"])
            reMat[index,3] = float(row["gjbdlbz"])
            reMat[index,4] = float(row["gjbdfsbz"])
            reMat[index,5] = float(row["gjsdebz"])
            reMat[index,6] = float(row["gjsdlbz"])
            reMat[index,7] = float(row["gjsdfsbz"])
            reMat[index,8] = float(row["zjbdebz"])
            reMat[index,9] = float(row["zjbdlbz"])
            reMat[index,10] = float(row["zjbdfsbz"])
            reMat[index,11] = float(row["zjsdebz"])
            reMat[index,12] = float(row["zjsdlbz"])
            reMat[index,13] = float(row["zjsdfsbz"])
            reMat[index,14] = float(row["djbdebz"])
            reMat[index,15] = float(row["djbdlbz"])
            reMat[index,16] = float(row["djbdfsbz"])
            reMat[index,17] = float(row["djsdebz"])
            reMat[index,18] = float(row["djsdlbz"])
            reMat[index,19] = float(row["djsdfsbz"])
            reMat[index,20] = float(row["glbdebz"])
            reMat[index,21] = float(row["glbdlbz"])
            reMat[index,22] = float(row["glbdfsbz"])
            reMat[index,23] = float(row["glsdebz"])
            reMat[index,24] = float(row["glsdlbz"])
            reMat[index,25] = float(row["glsdfsbz"])
            reMat[index,26] = float(row["zlbdebz"])
            reMat[index,27] = float(row["zlbdlbz"])
            reMat[index,28] = float(row["zlbdfsbz"])
            reMat[index,29] = float(row["zlsdebz"])
            reMat[index,30] = float(row["zlsdlbz"])
            reMat[index,31] = float(row["zlsdfsbz"])
            reMat[index,32] = float(row["dlbdebz"])
            reMat[index,33] = float(row["dlbdlbz"])
            reMat[index,34] = float(row["dlbdfsbz"])
            reMat[index,35] = float(row["dlsdebz"])
            reMat[index,36] = float(row["dlsdlbz"])
            reMat[index,37] = float(row["dlsdfsbz"])
            reMat[index,38] = float(row["zfza"])
            dmLables.append(row['dm'])
            reLables.append(row["zfz"])
            row = cursor.fetchone()
            index = index + 1
        cursor.close()
    except Exception,e:
        print '获取测试数据查询错误'
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
    return sortedClassCount[0][0],classObj[sortedClassCount[0][0]]
def classifyTest(ybsd,ybed,csd,my):
    '''
    ybsd  : 样本开始日期   ybed：样本结束日期，csd:测试数据日期 my: 我的个股清单
    '''
    g,l,r = selectALL(ybsd,ybed)
    sdate = csd
    tg,tl,tdm = selectTopTest(sdate)
    error = 0
    zj = 0
    mbz = []
    mymbz = []
    for i in range(0,len(tg[...,0])):
        cstl,reobj = classify1(tg[i,...],g,l,r,10)
        zcs = float(len(reobj))
#         db = Mysql.getConn()
#         cursor = db.cursor()
#         sql = '''
#            delete from gl_mem where  dm='%s' and jyrq = '%s';
#             ''' % (tdm[zj],sdate)
# #                 print sql
# #             sql = sql.encode("utf8")
#         cursor.execute(sql)
#         cursor.close()
#         db.commit()
#         gl = {"P00":0,"P01":0,"P02":0,"P03":0,"P04":0,"P05":0,"P06":0,"P07":0,"P08":0,"P09":0,"P010":0,"P10":0,"P20":0,"P30":0,"P40":0,"P50":0,"P60":0,"P70":0,"P80":0,"P90":0,"P100":0}
#         zfzh = 0.0
#         zfzcs = 0.0
#         sjz = 0.0
#         for o in reobj:
#             try:
#                 csdmrq = o.split('_')
#                 cursor = db.cursor()
#                 sql = '''
#                    select zfz from fscjmxhz_mem where  dm='%s' and jyrq > '%s'
# order by jyrq asc limit 3;
#                     ''' % (csdmrq[0],csdmrq[1])
# #                 print sql
#     #             sql = sql.encode("utf8")
#                 cursor.execute(sql)
#                 row = cursor.fetchone()
#                 while row is not None:
#                     if row['zfz'] == 0:
#                         gl["P00"] = gl.get("P00",0) + 1
#                     elif row["zfz"] >= -1 and row["zfz"] < 0:
#                         gl["P01"] = gl.get("P01",0) + 1
#                     elif row["zfz"] >= -2 and row["zfz"] < -1:
#                         gl["P02"] = gl.get("P02",0) + 1
#                     elif row["zfz"] >= -3 and row["zfz"] < -2:
#                         gl["P03"] = gl.get("P03",0) + 1
#                     elif row["zfz"] >= -4 and row["zfz"] < -3:
#                         gl["P04"] = gl.get("P04",0) + 1
#                     elif row["zfz"] >= -5 and row["zfz"] < -4:
#                         gl["P05"] = gl.get("P05",0) + 1
#                     elif row["zfz"] >= -6 and row["zfz"] < -5:
#                         gl["P06"] = gl.get("P06",0) + 1
#                     elif row["zfz"] >= -7 and row["zfz"] < -6:
#                         gl["P07"] = gl.get("P07",0) + 1
#                     elif row["zfz"] >= -8 and row["zfz"] < -7:
#                         gl["P08"] = gl.get("P08",0) + 1
#                     elif row["zfz"] >= -9 and row["zfz"] < -8:
#                         gl["P09"] = gl.get("P09",0) + 1
#                     elif row["zfz"] < -9:
#                         gl["P010"] = gl.get("P010",0) + 1
#                     elif row["zfz"] <=1  and row["zfz"] > 0:
#                         gl["P10"] = gl.get("P10",0) + 1
#                     elif row["zfz"] <=2  and row["zfz"] > 1:
#                         gl["P20"] = gl.get("P20",0) + 1
#                     elif row["zfz"] <= 3 and row["zfz"] > 2:
#                         gl["P30"] = gl.get("P30",0) + 1
#                     elif row["zfz"] <= 4 and row["zfz"] > 3:
#                         gl["P40"] = gl.get("P40",0) + 1
#                     elif row["zfz"] <= 5 and row["zfz"] > 4:
#                         gl["P50"] = gl.get("P50",0) + 1
#                     elif row["zfz"] <= 6 and row["zfz"] > 5:
#                         gl["P60"] = gl.get("P60",0) + 1
#                     elif row["zfz"] <= 7 and row["zfz"] > 6:
#                         gl["P70"] = gl.get("P70",0) + 1
#                     elif row["zfz"] <= 8 and row["zfz"] > 7:
#                         gl["P80"] = gl.get("P80",0) + 1
#                     elif row["zfz"] <= 9 and row["zfz"] > 8:
#                         gl["P90"] = gl.get("P90",0) + 1
#                     elif row["zfz"] > 9:
#                         gl["P110"] = gl.get("P110",0) + 1
#                     zfzcs = zfzcs + 1.0
#                     zfzh = zfzh + row["zfz"]
#                     row = cursor.fetchone()
#                 cursor.close()
# 
#             except Exception,e:
#                 print '数据查询错误'
#                 print e
#         try:
#             csdmrq = o.split('_')
#             cursor = db.cursor()
#             sql = '''
#                INSERT GL_MEM(DM,
# JYRQ ,
# P00 ,
# P01 ,
# P02 ,
# P03 ,
# P04 ,
# P05 ,
# P06 ,
# P07 ,
# P08 ,
# P09 ,
# P010 ,
# P10 ,
# P20 ,
# P30 ,
# P40 ,
# P50 ,
# P60 ,
# P70 ,
# P80 ,
# P90 ,
# P100,MB) VALUES('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
#                 ''' % (tdm[zj],sdate,gl["P00"]/zfzcs,gl["P01"]/zfzcs,gl["P02"]/zfzcs,gl["P03"]/zfzcs,gl["P04"]/zfzcs,gl["P05"]/zfzcs,gl["P06"]/zfzcs,gl["P07"]/zfzcs,gl["P08"]/zfzcs,gl["P09"]/zfzcs,gl["P010"]/zfzcs,gl["P10"]/zfzcs,gl["P20"]/zfzcs,gl["P30"]/zfzcs,gl["P40"]/zfzcs,gl["P50"]/zfzcs,gl["P60"]/zfzcs,gl["P70"]/zfzcs,gl["P80"]/zfzcs,gl["P90"]/zfzcs,gl["P100"]/zfzcs,zfzh/zfzcs)
# #                 print sql
# #             sql = sql.encode("utf8")
#             cursor.execute(sql)
#             cursor.close()
#             db.commit()
#         except Exception,e:
#             print '数据查询错误'
#             print e
#         cstl = zfzh/zfzcs
#         try:
#             csdmrq = o.split('_')
#             cursor = db.cursor()
#             sql = '''
#                select zfz as zfz from fscjmxhz_mem where  dm='%s' and jyrq > '%s'
# order by jyrq asc limit 3;
#                 ''' % (tdm[zj],sdate)
# #                 print sql
# #             sql = sql.encode("utf8")
#             cursor.execute(sql)
#             row = cursor.fetchone()
#             if row["zfz"] is not None:
#                 sjz = row["zfz"]
#             cursor.close
#         except Exception,e:
#             print '数据查询错误'
#             print e
#             sjz = 0
#         db.close()
        sjz = tl[zj]
        print tdm[zj],cstl,sjz
#         if (cstl < sjz and math.fabs(cstl - sjz) < 2) or (cstl >=sjz and math.fabs(cstl - sjz) < 1):
#             print u'%s:事实:%s   评估:%s   ok'  % (tdm[zj],sjz,cstl)
#         else:
#             print u'%s:事实:%s   评估:%s   error'  % (tdm[zj],sjz,cstl)
#             error = error + 1
             
        if cstl >= 7:
            mbz.append([tdm[zj],cstl,sjz])
            if cstl <= sjz:
                print u'%s>:事实:%s   评估:%s   ok'  % (tdm[zj],sjz,cstl)
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
        if tdm[zj] in my:
            mymbz.append([tdm[zj],cstl,sjz])
        zj = zj + 1
    print '代码   | 评估涨幅 | 实际涨幅\n' 
    for i in mbz:
        print '%s   |   %s   |   %s\n'  % (i[0],i[1],i[2])
    for i in mymbz:
        print '%s   |   %s   |   %s\n'  % (i[0],i[1],i[2])
    print "error rate:   %s"  % (error/float(len(mbz))) ,sdate
    
classifyTest('20150302','20150402','20150409',['002594','000906']) 

'''
Created on 2015年3月27日
流速流量模型  收盘后预测，前提已经转换好数据
@author: nimrob
'''