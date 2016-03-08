#-*-coding:UTF-8-*-#
'''
Created on 2015-4-21

@author: wangyi
'''
import numpy as np
import time
import math
from redline.dbhelper import Mysql
import os
import os.path
from datetime import datetime

h113000 = 1420084800.0
daysecond = 14700
daymm = 240.0
def ltgbf():
    db = Mysql.getConn()
    ltgbkv = {}
    zchzl = {}
    lrtb ={}
    srtb ={}
    jlrl ={}
    try:
        cursor = db.cursor()
        sql = '''
SELECT DM,AVG(LTGB) * 100 AS LTGB,ZCHZL,LRTB,SRTB,JLRL FROM HSAG GROUP BY DM;
            '''
#             print sql
#             sql = sql.encode("utf8")
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            ltgbkv[row["DM"]] = row["LTGB"]
            zchzl[row["DM"]] = row["ZCHZL"]
            lrtb[row["DM"]] = row["LRTB"]
            srtb[row["DM"]] = row["SRTB"]
            jlrl[row["DM"]] = row["JLRL"]
            row = cursor.fetchone()
        cursor.close()
    except Exception,e:
        print 'LTGB错误'
        print e
    db.close()
    return ltgbkv,zchzl,lrtb,srtb,jlrl
ltgb,zchzl,lrtb,srtb,jlrl = ltgbf()
def bstonum(s):
    s = s.decode('gbk').encode('utf8')
    flag = 0
    if s == '买盘':
        flag = 1
    if s == '卖盘':
        flag = -1
    return flag

def bstimetosn(s):
    retime = time.strptime('2015-01-01 %s' % s,"%Y-%m-%d %H:%M:%S")
    retime = math.fabs(time.mktime(retime))
    if retime > h113000:
        retime = retime - 5400.0
    return retime



def listfilename(rootdir):
    fullfilename = []
    for parent,dirnames,filenames in os.walk(rootdir):    
        for filename in filenames:                       
             fullfilename.append(os.path.join(parent,filename)) 
    return fullfilename

'''a file to database'''

def filetodb(fullfilename):
    db = Mysql.getConn()
    gpdm = fullfilename[-10:-4] 
    dt = fullfilename[-19:-11]
    fd = "%s-%s-%s" % (dt[0:4],dt[4:6],dt[6:8]) #yyyy-MM-dd

    try:
        c = np.loadtxt(fullfilename,delimiter='\t', skiprows=1,converters={0:bstimetosn,5:bstonum}, usecols=(0,1,2,3,4,5), unpack=False)
        d = np.fabs(np.diff(c[...,0]))
        d = np.hstack(([0],d))
        c[...,0] = d
        bze = np.sum(c[c[...,5]>0][...,4]) #买总额
        bzl = np.sum(c[c[...,5]>0][...,3]) #买总量
        sze = np.sum(c[c[...,5]<0][...,4]) #卖总额
        szl = np.sum(c[c[...,5]<0][...,3]) #卖总量
        pjbj = bze/bzl/ 100 #平均买价
        pjsj = sze/szl/ 100 #平均卖价
        pjjbz = pjbj/pjsj
        pjjcz = pjbj - pjsj
        pjbl = np.mean(c[c[...,5]>0][...,3])
        pjsl = np.mean(c[c[...,5]<0][...,3])
        pjlbz = pjbl/ pjsl
        pjlcz = pjbl - pjsl
        zxpl = np.sum(c[c[...,5]==0][...,3])
        zxpe = np.sum(c[c[...,5]==0][...,4])
        zxpbz = zxpl/(zxpl + bzl + szl)
        fzxpbz = 1.0 - zxpbz
        zxpebz = zxpe/(zxpe + bze + sze)
        ptp = np.ptp(c[...,1])
        min = np.min(c[...,1])
        h= ptp * 0.618
        h= h + min
        m= ptp * 0.382
        m = m + min
        tc = c[c[...,1]> h]
        gjbde = np.sum(tc[tc[...,5]> 0][...,4])
        gjbdl = np.sum(tc[tc[...,5]> 0][...,3])
        gjbdj = gjbde/gjbdl/100
        gjbdfs = np.sum(tc[tc[...,5]> 0][...,0]) 
        gjbdebz = gjbde/(zxpe + bze + sze)
        gjbdlbz = gjbdl/(zxpl + bzl + szl)
        gjbdfsbz = gjbdfs/daysecond 
        tc = c[c[...,1]> h]
        gjsde = np.sum(tc[tc[...,5]< 0][...,4])
        gjsdl = np.sum(tc[tc[...,5]< 0][...,3])
        gjsdj = gjsde/gjsdl/100
        gjsdfs = np.sum(tc[tc[...,5]< 0][...,0])
        gjsdebz = gjsde/(zxpe + bze + sze)
        gjsdlbz = gjsdl/(zxpl + bzl + szl)
        gjsdfsbz = gjsdfs/daysecond 
        tc = c[c[...,1]< h]
        tc = tc[tc[...,1]>m]
        zjbde = np.sum(tc[tc[...,5]> 0][...,4])
        zjbdl = np.sum(tc[tc[...,5]> 0][...,3])
        zjbdj = zjbde/zjbdl/100
        zjbdfs = np.sum(tc[tc[...,5]> 0][...,0]) 
        zjbdebz = zjbde/(zxpe + bze + sze)
        zjbdlbz = zjbdl/(zxpl + bzl + szl)
        zjbdfsbz = zjbdfs/daysecond 
        
        tc = c[c[...,1]< h]
        tc = tc[tc[...,1]>m]
        zjsde = np.sum(tc[tc[...,5]< 0][...,4])
        zjsdl = np.sum(tc[tc[...,5]< 0][...,3])
        zjsdj = zjsde/zjsdl/100
        zjsdfs = np.sum(tc[tc[...,5]< 0][...,0])
        zjsdebz = zjsde/(zxpe + bze + sze)
        zjsdlbz = zjsdl/(zxpl + bzl + szl)
        zjsdfsbz = zjsdfs/daysecond 

        tc = c[c[...,1]< m]
        djbde = np.sum(tc[tc[...,5]> 0][...,4])
        djbdl = np.sum(tc[tc[...,5]> 0][...,3])
        djbdj = djbde/djbdl/100
        djbdfs = np.sum(tc[tc[...,5]> 0][...,0]) 
        djbdebz = djbde/(zxpe + bze + sze)
        djbdlbz = djbdl/(zxpl + bzl + szl)
        djbdfsbz = djbdfs/daysecond 
        
        tc = c[c[...,1]< m]
        djsde = np.sum(tc[tc[...,5]< 0][...,4])
        djsdl = np.sum(tc[tc[...,5]< 0][...,3])
        djsdj = djsde/djsdl/100
        djsdfs = np.sum(tc[tc[...,5]< 0][...,0])
        djsdebz = djsde/(zxpe + bze + sze)
        djsdlbz = djsdl/(zxpl + bzl + szl)
        djsdfsbz = djsdfs/daysecond 
        
        lh = (pjbl + pjsl) * 0.618
        lm = (pjbl + pjsl) * 0.382

        tc = c[c[...,3]> lh]
        glbde = np.sum(tc[tc[...,5]> 0][...,4])
        glbdl = np.sum(tc[tc[...,5]> 0][...,3])
        glbdj = glbde/glbdl/100
        glbdfs = np.sum(tc[tc[...,5]> 0][...,0]) 
        glbdebz = glbde/(zxpe + bze + sze)
        glbdlbz = glbdl/(zxpl + bzl + szl)
        glbdfsbz = glbdfs/daysecond  
        
        tc = c[c[...,3]> lh]
        glsde = np.sum(tc[tc[...,5]< 0][...,4])
        glsdl = np.sum(tc[tc[...,5]< 0][...,3])
        glsdj = glsde/glsdl/100
        glsdfs = np.sum(tc[tc[...,5]< 0][...,0])
        glsdebz = glsde/(zxpe + bze + sze)
        glsdlbz = glsdl/(zxpl + bzl + szl)
        glsdfsbz = glsdfs/daysecond 
        
        tc = c[c[...,3]< lh]
        tc = tc[tc[...,3]>lm]
        zlbde = np.sum(tc[tc[...,5]> 0][...,4])
        zlbdl = np.sum(tc[tc[...,5]> 0][...,3])
        zlbdj = zlbde/zlbdl/100
        zlbdfs = np.sum(tc[tc[...,5]> 0][...,0]) 
        zlbdebz = zlbde/(zxpe + bze + sze)
        zlbdlbz = zlbdl/(zxpl + bzl + szl)
        zlbdfsbz = zlbdfs/daysecond 
        
        tc = c[c[...,3]< lh]
        tc = tc[tc[...,3]>lm]
        zlsde = np.sum(tc[tc[...,5]< 0][...,4])
        zlsdl = np.sum(tc[tc[...,5]< 0][...,3])
        zlsdj = zlsde/zlsdl/100
        zlsdfs = np.sum(tc[tc[...,5]< 0][...,0])
        zlsdebz = zlsde/(zxpe + bze + sze)
        zlsdlbz = zlsdl/(zxpl + bzl + szl)
        zlsdfsbz = zlsdfs/daysecond

        tc = c[c[...,3]< lm]
        dlbde = np.sum(tc[tc[...,5]> 0][...,4])
        dlbdl = np.sum(tc[tc[...,5]> 0][...,3])
        dlbdj = dlbde/dlbdl/100
        dlbdfs = np.sum(tc[tc[...,5]> 0][...,0]) 
        dlbdebz = dlbde/(zxpe + bze + sze)
        dlbdlbz = dlbdl/(zxpl + bzl + szl)
        dlbdfsbz = dlbdfs/daysecond 
        
        tc = c[c[...,3]< lm]
        dlsde = np.sum(tc[tc[...,5]< 0][...,4])
        dlsdl = np.sum(tc[tc[...,5]< 0][...,3])
        dlsdj = dlsde/dlsdl/100
        dlsdfs = np.sum(tc[tc[...,5]< 0][...,0])
        dlsdebz = dlsde/(zxpe + bze + sze)
        dlsdlbz = dlsdl/(zxpl + bzl + szl)
        dlsdfsbz = dlsdfs/daysecond
        
        zs = c[0,1] -c[0,2]
        jk = c[0,1]
        zg = np.max(c[...,1])
        zd = np.min(c[...,1])
        zf = np.sum(c[...,2])
        zfz = zf/zs * 100
        js = c[-1,1]
        cjl = np.sum(c[...,3])
        cje = np.sum(c[...,4])
        upe = np.sum(c[c[...,2]> 0][...,4])#资金流入金额
        upl = np.sum(c[c[...,2]> 0][...,3])#资金流入股份
        uped = np.sum(c[c[...,2]> 0][...,2])# 流入上涨价格变动累积
        uptd = np.sum(c[c[...,2]> 0][...,0])# 流入的时间累积
        upepj = upe/(uped * 100) #每涨1分钱所花的金额（分）
        uplpj = upl/(uped * 100) #每涨1分所花的股份（股）
        uptpj = uptd/(uped * 100) #每涨1分所花的时间（秒）
        downe =  np.sum(c[c[...,2]< 0][...,4])#资金流出金额
        downl =  np.sum(c[c[...,2]< 0][...,3])#资金流出股份
        downed =  np.sum(c[c[...,2]< 0][...,2])#流出下降价格变动累积
        downtd =  np.sum(c[c[...,2]< 0][...,0])#流出下降时间累积
        downepj = downe/(downed * 100) #每涨1分钱所花的金额（分）
        downlpj = downl/(downed * 100) #每涨1分所花的股份（股）
        downtpj = downtd/(downed * 100) #每涨1分所花的时间（秒）
        jlr = upe - downe
        mcjl = cjl / daymm
        mcje = cje /daymm
        mbs = bzl /daymm
        mss = szl /daymm
        mups = uped /daymm
        mdowns = downed /daymm
        nzfz = 0.0
        nb = 0.0
        hsl = cjl/ltgb[gpdm]
        try:
            cursor = db.cursor()            
            sql = "DELETE FROM FSCJMXHZ_MEM WHERE DM='%s' AND JYRQ='%s';" % (gpdm,fd)
            cursor.execute(sql)
    
        except Exception,e:
            pass
        cursor.close()
        db.commit()
        try:
            cursor = db.cursor()            
            sql = '''INSERT FSCJMXHZ_MEM (
    DM,
    JYRQ,
    BZE ,
    BZL ,
    SZE ,
    SZL ,
    PJBJ ,
    PJSJ ,
    PJJBZ ,
    PJJCZ ,
    PJBL ,
    PJSL ,
    PJLBZ ,
    PJLCZ ,
    ZXPL ,
    ZXPBZ ,
    FZXPBZ ,
    ZXPE ,
    ZXPEBZ ,
    H ,
    M ,
    GJBDE ,
    GJBDJ ,
    GJBDL ,
    GJBDFS ,
    GJBDEBZ ,
    GJBDLBZ ,
    GJBDFSBZ ,
    GJSDE ,
    GJSDJ ,
    GJSDL ,
    GJSDFS ,
    GJSDEBZ ,
    GJSDLBZ ,
    GJSDFSBZ ,
    ZJBDE ,
    ZJBDJ ,
    ZJBDL ,
    ZJBDFS ,
    ZJBDEBZ ,
    ZJBDLBZ ,
    ZJBDFSBZ ,
    ZJSDE ,
    ZJSDJ ,
    ZJSDL ,
    ZJSDFS ,
    ZJSDEBZ ,
    ZJSDLBZ ,
    ZJSDFSBZ ,
    DJBDE ,
    DJBDJ ,
    DJBDL ,
    DJBDFS ,
    DJBDEBZ ,
    DJBDLBZ ,
    DJBDFSBZ ,
    DJSDE ,
    DJSDJ ,
    DJSDL ,
    DJSDFS ,
    DJSDEBZ ,
    DJSDLBZ ,
    DJSDFSBZ ,
    LH ,
    LM ,
    GLBDE ,
    GLBDJ ,
    GLBDL ,
    GLBDFS ,
    GLBDEBZ ,
    GLBDLBZ ,
    GLBDFSBZ ,
    GLSDE ,
    GLSDJ ,
    GLSDL ,
    GLSDFS ,
    GLSDEBZ ,
    GLSDLBZ ,
    GLSDFSBZ ,
    ZLBDE ,
    ZLBDJ ,
    ZLBDL ,
    ZLBDFS ,
    ZLBDEBZ ,
    ZLBDLBZ ,
    ZLBDFSBZ ,
    ZLSDE ,
    ZLSDJ ,
    ZLSDL ,
    ZLSDFS ,
    ZLSDEBZ ,
    ZLSDLBZ ,
    ZLSDFSBZ ,
    DLBDE ,
    DLBDJ ,
    DLBDL ,
    DLBDFS ,
    DLBDEBZ ,
    DLBDLBZ ,
    DLBDFSBZ ,
    DLSDE ,
    DLSDJ ,
    DLSDL ,
    DLSDFS ,
    DLSDEBZ ,
    DLSDLBZ ,
    DLSDFSBZ ,
    ZS ,
    JK ,
    ZG ,
    ZD ,
    JS,
    ZF ,
    ZFZ ,
    CJL ,
    CJE ,
    UPE ,
    UPL ,
    UPED ,
    UPTD ,
    UPEPJ ,
    UPLPJ ,
    UPTPJ ,
    DOWNE ,
    DOWNL ,
    DOWNED ,
    DOWNTD ,
    DOWNEPJ ,
    DOWNLPJ ,
    DOWNTPJ ,
    JLR ,
    MCJL ,
    MCJE ,
    MBS ,
    MSS ,
    MUPS ,
    MDOWNS,
    NB,
    HSL,
    NZFZ 
    ) values('%s','%s',
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s
    );''' % (gpdm,
    fd,
    bze ,
    bzl ,
    sze ,
    szl ,
    pjbj ,
    pjsj ,
    pjjbz ,
    pjjcz ,
    pjbl ,
    pjsl ,
    pjlbz ,
    pjlcz ,
    zxpl ,
    zxpbz ,
    fzxpbz ,
    zxpe ,
    zxpebz ,
    h ,
    m ,
    gjbde ,
    gjbdj ,
    gjbdl ,
    gjbdfs ,
    gjbdebz ,
    gjbdlbz ,
    gjbdfsbz ,
    gjsde ,
    gjsdj ,
    gjsdl ,
    gjsdfs ,
    gjsdebz ,
    gjsdlbz ,
    gjsdfsbz ,
    zjbde ,
    zjbdj ,
    zjbdl ,
    zjbdfs ,
    zjbdebz ,
    zjbdlbz ,
    zjbdfsbz ,
    zjsde ,
    zjsdj ,
    zjsdl ,
    zjsdfs ,
    zjsdebz ,
    zjsdlbz ,
    zjsdfsbz ,
    djbde ,
    djbdj ,
    djbdl ,
    djbdfs ,
    djbdebz ,
    djbdlbz ,
    djbdfsbz ,
    djsde ,
    djsdj ,
    djsdl ,
    djsdfs ,
    djsdebz ,
    djsdlbz ,
    djsdfsbz ,
    lh ,
    lm ,
    glbde ,
    glbdj ,
    glbdl ,
    glbdfs ,
    glbdebz ,
    glbdlbz ,
    glbdfsbz ,
    glsde ,
    glsdj ,
    glsdl ,
    glsdfs ,
    glsdebz ,
    glsdlbz ,
    glsdfsbz ,
    zlbde ,
    zlbdj ,
    zlbdl ,
    zlbdfs ,
    zlbdebz ,
    zlbdlbz ,
    zlbdfsbz ,
    zlsde ,
    zlsdj ,
    zlsdl ,
    zlsdfs ,
    zlsdebz ,
    zlsdlbz ,
    zlsdfsbz ,
    dlbde ,
    dlbdj ,
    dlbdl ,
    dlbdfs ,
    dlbdebz ,
    dlbdlbz ,
    dlbdfsbz ,
    dlsde ,
    dlsdj ,
    dlsdl ,
    dlsdfs ,
    dlsdebz ,
    dlsdlbz ,
    dlsdfsbz ,
    zs ,
    jk ,
    zg ,
    zd ,
    js ,
    zf ,
    zfz ,
    cjl,
    cje ,
    upe ,
    upl ,
    uped ,
    uptd ,
    upepj ,
    uplpj ,
    uptpj ,
    downe ,
    downl ,
    downed ,
    downtd ,
    downepj ,
    downlpj ,
    downtpj ,
    jlr,
    mcjl ,
    mcje ,
    mbs ,
    mss ,
    mups,
    mdowns,
    nb,
    hsl,
    nzfz)
#             print sql
            cursor.execute(sql)
            cursor.close()
            db.commit()
        except Exception,e:
            print '导入文件错误:%s' % fullfilename,e
        db.close()
    except Exception,e:
        print e
    print 'import a file',fullfilename

def ci(currToday):
    files = listfilename("/home/wangyi/gp/DOWNCJMX/%s" % currToday)
    print 'begin'
    for file in files:
        filetodb(file)
    print 'end'

if __name__ == '__main__':
#     files = listfilename("/home/wangyi/gp/CJMX/201505/%s" % datetime.strftime(datetime.now(),'%Y%m%d'))
    files = listfilename("/home/wangyi/gp/DOWNCJMX")
    print 'begin'
    for file in files:
        filetodb(file)
    print 'end'
        