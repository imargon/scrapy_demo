#-*-coding:UTF-8-*-#
'''
Created on 2015-3-6

@author: wangyi
'''
import numpy as np
import time
import math
from dbhelper import Mysql
import database
import os
import os.path
import urllib
import urllib2
import hashlib
from datetime import datetime
h113000 = 1420084800.0
daysecond = 14700

h113000 = 1420084800.0
daysecond = 14700

def bstonum(s):
    s = s.decode('gbk').encode('utf8')
    flag = 0
    if s == 'B':
        flag = 1
    if s == 'S':
        flag = -1
    return flag

def bstimetosn(s):
    retime = time.strptime('2015-01-01 %s' % s,"%Y-%m-%d %H:%M:%S")
    retime = math.fabs(time.mktime(retime))
    if retime > h113000:
        retime = retime - 5400.0
    return retime

def numrgo(gpdm,dt):
    db = Mysql.getConn()
    dm = ''
    if gpdm[0] == '0':
        dm = 'sz' + gpdm 
    else:
        dm ='sh' + gpdm 
    fd = "%s-%s-%s" % (dt[0:4],dt[4:6],dt[6:8]) #yyyy-MM-dd
    try:
        turl = "http://stock.gtimg.cn/data/index.php?appn=detail&action=timeline&c=%s"
        durl = "http://stock.gtimg.cn/data/index.php?appn=detail&action=data&c=%s&p=%s"
        
        try:
            req = urllib2.Request(turl % dm)
            res_data = urllib2.urlopen(req)
            res = res_data.read()
            dd = None
            jj =0
            for line in res.split('|'):
                try:
                    durl_g = durl % (dm,jj)
                    hash_durl = hashlib.md5(durl_g).hexdigest()
                    if database.exists(hash_durl):
                        dres = database.get(hash_durl)
                    else:
                        req = urllib2.Request(durl_g)
                        res_data = urllib2.urlopen(req)
                        dres = res_data.read()
                        database.set(hash_durl,dres)
                    dres = dres.split(',')[1]
                    dres = dres[1:-2]
                    dres = dres.split('|')
                    dim = len(dres)
                    c = np.empty([dim,6],float)
                    ff = 0
#                     print dres
                    for l1 in dres:
                        ll2 =  l1.split('/')
                        c[ff,0] = bstimetosn(ll2[1])
                        c[ff,1]= float(ll2[2])
                        c[ff,2]=float(ll2[3])
                        c[ff,3]=float(ll2[4])
                        c[ff,4]=float(ll2[5])
                        c[ff,5]=bstonum(ll2[6])
                        ff = ff + 1
                    if dd is not None:
                        dd = np.vstack((dd,c))
                    else:
                        dd = c
                                
                except Exception,e:
                    print e
                jj = jj + 1
        except Exception,e:
            pass
        c = dd #np.loadtxt(fullfilename,delimiter='\t', skiprows=5,converters={0:bstimetosn,4:bstonum}, usecols=(0,1,2,3,4), unpack=False)
        f = np.reshape(c[...,0],(len(c[...,0]),1))
        c = np.hstack((c,f))
        d = np.fabs(np.diff(c[...,0]))
        d = np.hstack(([0],d))
        c[...,0] = d

        bze = np.sum(c[c[...,5]>0][...,4])
        bzl = np.sum(c[c[...,5]>0][...,3])
        sze = np.sum(c[c[...,5]<0][...,4])
        szl = np.sum(c[c[...,5]<0][...,3])
        pjbj = bze/bzl/ 100
        pjsj = sze/szl/ 100
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
    #     print 'zs',zs
        jk = c[0,1]
    #     print 'jk',jk
        zg = np.max(c[...,1])
    #     print 'zg',zg
        zd = np.min(c[...,1])
    #     print 'zd',zd
        zf = np.sum(c[...,2])
    #     print 'zf',zf
        zfz = zf/zs * 100
    #     print 'zfz',zfz
        js = c[-1,1]
        gjec = (gjbdebz - gjsdebz) * 100
        gjjc = gjbdj - gjsdj 
        gjlc = (gjbdlbz - gjsdlbz) * 100
        gjsc = (gjbdfsbz - gjsdfsbz) * 100
        
        zjec = (zjbdebz - zjsdebz) * 100 
        zjjc = zjbdj - zjsdj
        zjlc = (zjbdlbz - zjsdlbz) * 100
        zjsc = (zjbdfsbz - zjsdfsbz) * 100
         
        djec = (djbdebz -djsdebz) * 100
        djjc = djbdj - djsdj 
        djlc = (djbdlbz - djsdlbz) * 100
        djsc = (djbdfsbz - djsdfsbz) * 100
        
        glec = (glbdebz - glsdebz) * 100
        gljc = glbdj - glsdj
        gllc = (glbdlbz - glsdlbz) * 100
        glsc = (glbdfsbz - glsdfsbz) * 100
        
        zlec = (zlbdebz - zlsdebz ) * 100
        zljc = zlbdj - zlsdj
        zllc = (zlbdlbz - zlsdlbz) * 100
        zlsc = (zlbdfsbz - zlsdfsbz) * 100
        
        dlec = (dlbdebz - dlsdebz) * 100 
        dljc = dlbdj - dlsdj
        dllc = (dlbdlbz - dlsdlbz) * 100
        dlsc = (dlbdfsbz - dlsdfsbz) * 100
        
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
    GJEC ,
    GJJC ,
    GJLC ,
    GJSC ,
    ZJEC ,
    ZJJC ,
    ZJLC ,
    ZJSC ,
    DJEC ,
    DJJC ,
    DJLC ,
    DJSC ,
    GLEC ,
    GLJC ,
    GLLC ,
    GLSC ,
    ZLEC ,
    ZLJC ,
    ZLLC ,
    ZLSC ,
    DLEC ,
    DLJC ,
    DLLC ,
    DLSC 
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
    %s,%s,%s,%s,%s,%s
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
    gjec ,
    gjjc ,
    gjlc ,
    gjsc ,
    zjec ,
    zjjc ,
    zjlc ,
    zjsc ,
    djec ,
    djjc ,
    djlc ,
    djsc ,
    glec ,
    gljc ,
    gllc ,
    glsc ,
    zlec ,
    zljc ,
    zllc ,
    zlsc ,
    dlec ,
    dljc ,
    dllc ,
    dlsc )
#             print sql
            cursor.execute(sql)
            cursor.close()
            db.commit()
        except Exception,e:
            print '导入数据库错误:',e
        db.close()
    except Exception,e:
        print '导入出现错误：',e

def listfilename(rootdir):
    fullfilename = []
    for parent,dirnames,filenames in os.walk(rootdir):    
        for filename in filenames:                       
             fullfilename.append(os.path.join(parent,filename)) 
    return fullfilename

'''a file to database'''

def filetodb(fullfilename):
    gpdm = fullfilename[-10:-4] 
    numrgo(gpdm,datetime.strftime(datetime.now(),'%Y%m%d'))
    print 'import a file',fullfilename
    
# this only runs if the module was *not* imported
if __name__ == '__main__':
#     files = listfilename("d:\\gp\\002297")
#     print files 
#     print files[0]
#     print files[0][-10:-4]
#     d = files[0][-19:-11]
#     print d
#     fd = "%s-%s-%s" % (d[0:4],d[4:6],d[6:8])
#     print fd
    files = listfilename("/Users/nimrob/gp/D1/OVER")
    print 'begin'
    for file in files:
        filetodb(file)
    print 'end'
        