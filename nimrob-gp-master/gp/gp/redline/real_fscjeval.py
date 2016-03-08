#-*-coding:UTF-8-*-#
'''
Created on 2015年3月27日
实时预测分时成交结构
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
               from fscjmxhz_mem
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
        reMat = zeros((rdl,38))
        reLables = []
        reObjs = []
        index = 0
        try:
            cursor = db.cursor()
            sql = '''
               select d.pjjbz,d.pjlbz,d.dm,d.jyrq,
               d.gjbdebz,d.gjbdlbz,d.gjbdfsbz,
               d.gjsdebz,d.gjsdlbz,d.gjsdfsbz,
               d.zjbdebz,d.zjbdlbz,d.zjbdfsbz,
               d.zjsdebz,d.zjsdlbz,d.zjsdfsbz,
               d.djbdebz,d.djbdlbz,d.djbdfsbz,
               d.djsdebz,d.djsdlbz,d.djsdfsbz,
               d.glbdebz,d.glbdlbz,d.glbdfsbz,
               d.glsdebz,d.glsdlbz,d.glsdfsbz,
               d.zlbdebz,d.zlbdlbz,d.zlbdfsbz,
               d.zlsdebz,d.zlsdlbz,d.zlsdfsbz,
               d.dlbdebz,d.dlbdlbz,d.dlbdfsbz,
               d.dlsdebz,d.dlsdlbz,d.dlsdfsbz,floor(d.dlsc) as zfz,d.zfz/100.0 as zfza
               from fscjmxhz_mem as d 
               where d.jyrq >= '%s'  and d.jyrq <= '%s'; 
                ''' % (jyrq,jyrq2)
#             print sql
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
#                 reMat[index,38] = float(row["zfza"])
                reLables.append(row["zfz"])
                reObjs.append('%s_%s' % (row["dm"],datetime.strftime(row['jyrq'],'%Y-%m-%d')))
                row = cursor.fetchone()
                index = index + 1
            cursor.close()
        except Exception,e:
            print '数据查询错误'
            print e
        db.close()
        reMat = reMat[0:len(reLables),...]
        return reMat,reLables,reObjs

def selectTopTest(jyrq,rdl):
        db = Mysql.getConn()
        reMat = zeros((rdl,38))
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
               where a.jyrq = '%s'   limit %s;
                ''' % (jyrq,rdl)
#                left join ( 
#                 select dm,jyrq,zfz from fscjmxhz_mem 
#                 WHERE jyrq= (select jyrq from fscjmxhz_mem where jyrq > '%s' 
#     order by jyrq asc limit 1) 
#                 )
#                 as b 
#                on a.dm = b.dm
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
#                 reMat[index,38] = float(row["zfza"])
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
    tg,tl,tdm = selectTopTest(sdate,3000)
    error = 0
    zj = 0
    mbz = []
    mymbz = []
    for i in range(0,len(tg[...,0])):
        cstl,reobj = classify1(tg[i,...],g,l,r,10)
        zcs = float(len(reobj))
        sjz = tl[zj]
        if cstl >= -11 and cstl <= 11:
            mbz.append([tdm[zj],cstl,sjz])
            if cstl <= sjz:
                print u'%s:事实:%s   评估:%s   ok'  % (tdm[zj],sjz,cstl)
            else:
                print u'%s:事实:%s   评估:%s   error'  % (tdm[zj],sjz,cstl)
                error = error + 1
            db = Mysql.getConn()
            cursor = db.cursor()
            sql = '''
               delete from gl_mem where  dm='%s' and jyrq = '%s';
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
                   INSERT GL_MEM(DM,
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
    
classifyTest('20150105','20150410','20150416',['002289','600736','600512','000858']) 

