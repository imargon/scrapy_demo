#-*-coding:UTF-8-*-#
'''
Created on 2015-3-6

@author: wangyi
'''
import numpy as np
import time
import math
from dbhelper import Mysql
import os
import os.path
from datetime import datetime
h113000 = 1420084800.0
daysecond = 14700

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

def numpyproc(tn):
    sp = tn[-1,1]
    bh = np.sum(tn[...,2])
    cjl = np.sum(tn[...,3])
    cje = np.sum(tn[...,4])
    try:
        sl = np.sum(tn[tn[...,5]< 0][...,3])
        se = np.sum(tn[tn[...,5]< 0][...,4])
        ss = np.sum(tn[tn[...,5]< 0][...,0])
        if sl == 0 or ss == 0:
            msl = 0
        else:
            msl =  sl/ss
    except Exception,e:
        msl = 0
    try:
        sc = np.sum(tn[tn[...,2]< 0][...,2])
        ss = np.sum(tn[tn[...,2]< 0][...,0])
        if sc ==0 or ss == 0:
            mss = 0
        else:
            mss =  sc/ss 
    except Exception,e:
        mss = 0
    try:
        bl =  np.sum(tn[tn[...,5]> 0][...,3])
        be =  np.sum(tn[tn[...,5]> 0][...,4])
        bs =  np.sum(tn[tn[...,5]> 0][...,0])
        if bl ==0 or bs == 0:
            mbl = 0
        else:
            mbl =  bl/bs 
    except Exception,e:
        mbl = 0
    try:
        bc =  np.sum(tn[tn[...,2]> 0][...,2])
        bs =  np.sum(tn[tn[...,2]> 0][...,0])
        if bc == 0 or bs == 0:
            mbs = 0
        else:
            mbs =  bc/bs
    except Exception,e:
        mbs = 0
    mh = mbl * mbs + msl * mss
    return mbl,mbs,msl,mss,mh,cjl,bl,sl,cje,be,se,bh,sp

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
#     print gpdm,dt,fd
    try:
        c = np.loadtxt(fullfilename,delimiter='\t', skiprows=1,converters={0:bstimetosn,5:bstonum}, usecols=(0,1,2,3,4,5), unpack=False)
        f = np.reshape(c[...,0],(len(c[...,0]),1))
        c = np.hstack((c,f))
        d = np.fabs(np.diff(c[...,0]))
        d = np.hstack(([0],d))
        c[...,0] = d

        bs = int(bstimetosn("09:30:00"))
        es = int(bstimetosn('15:00:00'))
        mnum = 0
        sql = ""
        for i in range(bs,es,60):
            try:
                tnb = c[c[...,6] <= i]
                if i== bs:
                    ib= int(bstimetosn("09:20:00"))
                else:
                    ib = i -60
                tn = tnb[tnb[...,6] > ib]
                mnum = (i - bs) / 60 + 1
                mbl,mbs,msl,mss,mh,cjl,bl,sl,cje,be,se,bh,sp = numpyproc(tn)
                pmbl,pmbs,pmsl,pmss,pmh,pcjl,pbl,psl,pcje,pbe,pse,pbh,psp = numpyproc(tnb)
                sql = sql + "insert sdqs (dm,jyrq,mnum,mbl,mbs,msl,mss,mh,cjl,bl,sl,cje,be,se,bh,pmbl,pmbs,pmsl,pmss,pmh,pcjl,pbl,psl,pcje,pbe,pse,pbh,sp) values('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); " % (gpdm,fd,mnum,mbl,mbs,msl,mss,mh,cjl,bl,sl,cje,be,se,bh,pmbl,pmbs,pmsl,pmss,pmh,pcjl,pbl,psl,pcje,pbe,pse,pbh,sp)
#                 print sql
#                 print dysd,dysd1,tssd,tssd1, dysd * dysd1 + tssd * tssd1,"\n"
            except Exception,e:
                print e        
        try:
            cursor = db.cursor()            
            sqldel = "DELETE FROM sdqs WHERE DM='%s' AND JYRQ='%s';" % (gpdm,fd)
            cursor.execute(sqldel)
        except Exception,e:
            print e
        cursor.close()
        db.commit()
        try:
            cursor = db.cursor()            
            cursor.execute(sql)
            cursor.close()
            db.commit()
        except Exception,e:
            print '导入数据库错误:',e
        db.close()
    except Exception,e:
        print '导入出现错误：',e
    print 'import a file',fullfilename
if __name__ == '__main__':
#     files = listfilename("d:\\gp\\002297")
#     print files 
#     print files[0]
#     print files[0][-10:-4]
#     d = files[0][-19:-11]
#     print d
#     fd = "%s-%s-%s" % (d[0:4],d[4:6],d[6:8])
#     print fd
    files = listfilename("/home/wangyi/gp/CJMX/%s" % datetime.strftime(datetime.now(),'%Y%m%d'))
#     files = listfilename("/home/wangyi/gp/CJMX/%s" % '20150407')
#     files = listfilename("/home/wangyi/gp/CJMX/20150410")
    print 'begin'
    for file in files:
        filetodb(file)
    print 'end'
    
