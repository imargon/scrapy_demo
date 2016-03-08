#-*-coding:UTF-8-*-#
'''
Created on 2015年3月27日
每日概率反向验证
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
               from gl_mem
               where jyrq >= '%s'  and jyrq <  '%s' and jyrq !='%s'; 
                ''' % (jyrq,jyrq2,currdate)
#                 print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            rdl = row['ts']
            cursor.close()
        except Exception,e:
            print '数据查询错误'
            print e
        reMat = zeros((rdl,22))
        reLables = []
        reObjs = []
        index = 0
        try:
            cursor = db.cursor()
            sql = '''
select dm,jyrq,mb/100.0 as mb,p100,p90, p80, p70, p60, p50, p40, p30, p20, p10, p00, p01, p02, p03, p04, p05, p06, p07, p08, p09, p010,floor(nzfz) as zfz
from gl_mem  
where jyrq >= '%s'  and jyrq <=  '%s' and jyrq !='%s';
                ''' % (jyrq,jyrq2,currdate)
            print sql
#             sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["mb"])
                reMat[index,1] = float(row["p100"])
                reMat[index,2] = float(row["p90"])
                reMat[index,3] = float(row["p80"])
                reMat[index,4] = float(row["p70"])
                reMat[index,5] = float(row["p60"])
                reMat[index,6] = float(row["p50"])
                reMat[index,7] = float(row["p40"])
                reMat[index,8] = float(row["p30"])
                reMat[index,9] = float(row["p20"])
                reMat[index,10] = float(row["p10"])
                reMat[index,11] = float(row["p00"])
                reMat[index,12] = float(row["p01"])
                reMat[index,13] = float(row["p02"])
                reMat[index,14] = float(row["p03"])
                reMat[index,15] = float(row["p04"])
                reMat[index,16] = float(row["p05"])
                reMat[index,17] = float(row["p06"])
                reMat[index,18] = float(row["p07"])
                reMat[index,19] = float(row["p08"])
                reMat[index,20] = float(row["p09"])
                reMat[index,21] = float(row["p010"])
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
        reMat = zeros((rdl,22))
        reLables = []
        dmLables = []
        index = 0

        try:
            cursor = db.cursor()
            sql = '''
select dm,jyrq,mb/100.0 as mb,p100,p90, p80, p70, p60, p50, p40, p30, p20, p10, p00, p01, p02, p03, p04, p05, p06, p07, p08, p09, p010,floor(nzfz) as zfz
from gl_mem  
where jyrq = '%s'   limit %s;
                ''' % (jyrq,rdl)
            print sql
#                 sql = sql.encode("utf8")
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                reMat[index,0] = float(row["mb"])
                reMat[index,1] = float(row["p100"])
                reMat[index,2] = float(row["p90"])
                reMat[index,3] = float(row["p80"])
                reMat[index,4] = float(row["p70"])
                reMat[index,5] = float(row["p60"])
                reMat[index,6] = float(row["p50"])
                reMat[index,7] = float(row["p40"])
                reMat[index,8] = float(row["p30"])
                reMat[index,9] = float(row["p20"])
                reMat[index,10] = float(row["p10"])
                reMat[index,11] = float(row["p00"])
                reMat[index,12] = float(row["p01"])
                reMat[index,13] = float(row["p02"])
                reMat[index,14] = float(row["p03"])
                reMat[index,15] = float(row["p04"])
                reMat[index,16] = float(row["p05"])
                reMat[index,17] = float(row["p06"])
                reMat[index,18] = float(row["p07"])
                reMat[index,19] = float(row["p08"])
                reMat[index,20] = float(row["p09"])
                reMat[index,21] = float(row["p010"])
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
    g,l,r = selectALL(ybsd,ybed,csd)
    sdate = csd
    tg,tl,tdm = selectTopTest(sdate,3000)
    error = 0
    zj = 0
    mbz = []
    db = Mysql.getConn()
    for i in range(0,len(tg[...,0])):
        cstl,reobj = classify1(tg[i,...],g,l,r,kvalue)
        zcs = float(len(reobj))
        sjz = tl[zj]
        if cstl >= -11 and cstl <= 11 or (tdm[zj] in my):
            mbz.append([tdm[zj],cstl,sjz])
            if cstl <= sjz:
                print u'%s:事实:%s   评估:%s   ok'  % (tdm[zj],sjz,cstl)
            else:
                print u'%s:事实:%s   评估:%s   error'  % (tdm[zj],sjz,cstl)
                error = error + 1
            try:
                cursor = db.cursor()
                sql = '''
                   INSERT GL_EVAL(DM,JYRQ,MB) VALUES('%s','%s',%s);
                    ''' % (tdm[zj],sdate,cstl)
    #                 print sql
    #             sql = sql.encode("utf8")
                cursor.execute(sql)
                cursor.close()
                db.commit()
            except Exception,e:
                print '数据查询错误'
                print e
        zj = zj + 1
    print '代码   | 评估涨幅 | 实际涨幅\n' 
    for i in mbz:
        print '%s   |   %s   |   %s\n'  % (i[0],i[1],i[2])
    print "error rate:   %s"  % (error/float(len(mbz))) ,sdate

def yzmb(jyrq):
    db = Mysql.getConn()
    mblist = []
    try:
        mbsql ='''
         select DM,round((P100 + P90 + P80)*100,2) as P80,
        round((P40 + P30 + P20 + P10 + p00 + P70 + P60 + P50)*100,2) as P10,
        round((P01 + P02 + P03 + P04 + P07 + P06 + P05)*100,2) as P01,
        round((P010 + P09 + P08 )*100,2) as P08,
        MB,NZFZ
        from gl_mem where JYRQ='%s' and mb >=3 order by (MB *10 + P80 * 6 +P10 *2-P08-P01)/20 desc  limit 200;
        ''' % jyrq
        cursor = db.cursor()
        cursor.execute(mbsql)
        row = cursor.fetchone()
        while row is not None:
            mblist.append(row['DM'])
            row = cursor.fetchone()
        cursor.close()
    except Exception,e:
        print '数据查询错误'
        print e
    db.close()
    return mblist
def ge(currToday):
    classifyTest('20150106',currToday,currToday,yzmb(currToday))
'''
概率评估指定天的下一日涨幅 
'''
if __name__ == '__main__':
    curr = datetime.strftime(datetime.now(),'%Y%m%d')
#     curr='20150522'
    classifyTest('20150106',curr,curr,yzmb(curr))
    # db = Mysql.getConn()
    # try:
    #     cursor = db.cursor()
    #     sql = '''
    #         SELECT JYRQ FROM NEXTJYRQ;
    #         '''
    # #   print sql
    # #   sql = sql.encode("utf8")
    #     cursor.execute(sql)
    #     row = cursor.fetchone()
    #     while row is not None:
    #         csmbdate = row["JYRQ"]
    #         classifyTest('20150106','20150421',csmbdate,yzmb(csmbdate))
    #         row = cursor.fetchone()
    #     cursor.close()
    #     db.commit()
    # except Exception,e:
    #     print e
    # db.close()
'''
Created on 2015年3月27日
每日历史结构评估概率反向验证
@author: nimrob
'''
