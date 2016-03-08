#-*-coding:UTF-8-*-#
'''
Created on 2015-3-6
M5数据导入
@author: wangyi
'''
from redline.dbhelper import Mysql

import os
import os.path
from datetime import datetime
def listfilename(rootdir):
    fullfilename = []
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     for dirname in  dirnames:                       #输出文件夹信息
#         print "parent is:" + parent
#         print  "dirname is" + dirname
#     print 'files:'
    
        for filename in filenames:                        #输出文件信息
    #         print "parent is" + parent
    #         print "filename is:" + filename
             fullfilename.append(os.path.join(parent,filename)) #输出文件路径信息
    return fullfilename

'''a file to database'''

def filetodb(fullfilename):
    f = open(fullfilename)
    line = f.readline()
    db = Mysql.getConn()#获取池中连接
#     gpdm = fullfilename[-12:-4] #股票代码获取带交易所
    dm = fullfilename[-10:-4] #股票代码获取
    #没有数据表就创建
    cursor = db.cursor()            
    sql = '''
CREATE TABLE if not exists M5%s(
    DM varchar(10) NULL,
    JYRQ datetime NOT NULL,
    KP float NULL,
    ZG float NULL,
    ZD float NULL,
    SP float NULL,
    CJL float NULL,
    CJE float NULL,
    MA5 float NULL,
    MA10 float NULL,
    MA20 float NULL,
    MA60 float NULL,
    MACD_DIF float NULL,
    MACD_DEA float NULL,
    VOL_TDX_VOLUME float NULL,
    VOL_TDX_MAVOL1 float NULL,
    VOL_TDX_MAVOL2 float NULL,
    WR1 float NULL,
    WR2 float NULL,
    BOLL float NULL,
    BOLL_UB float NULL,
    BOLL_LB float NULL,
    DMI_PDI float NULL,
    DMI_MDI float NULL,
    DMI_ADX float NULL,
    DMI_ADXR float NULL,
    DMA_DIF float NULL,
    DMA_DIFMA float NULL,
    FSL_SWL float NULL,
    FSL_SWS float NULL,
    TRIX float NULL,
    MATRIX float NULL,
    BR float NULL,
    AR float NULL,
    CR float NULL,
    CR_MA1 float NULL,
    CR_MA2 float NULL,
    CR_MA3 float NULL,
    CR_MA4 float NULL,
    VR float NULL,
    MAVR float NULL,
    OBV float NULL,
    MAOBV float NULL,
    ASI float NULL,
    MAASI float NULL,
    EMV float NULL,
    MAEMV float NULL,
    RSI1 float NULL,
    RSI2 float NULL,
    RSI3 float NULL,
    K float NULL,
    D float NULL,
    J float NULL,
    CCI float NULL,
    ROC float NULL,
    MAROC float NULL,
    MTM float NULL,
    MAMTM float NULL,
    PSY float NULL,
    MAPSY float NULL,
    WY1 float NULL,
    WY2 float NULL,
    WY3 float NULL,
    WY4 float NULL,
    WY5 float NULL,
    WY6 float NULL,
    WY7 float NULL,
    WY8 float NULL,
    WY9 float NULL,
    WY10 float NULL,
    WY11 float NULL,
    WY12 float NULL,
    WY13 float NULL,
    WY14 float NULL,
    WY15 float NULL,
    WY16 float NULL,
    WY17 float NULL,
    WY18 float NULL,
    SW1 float NULL,
    SW2 float NULL,
    SW3 float NULL,
    SW4 float NULL,
    SW5 float NULL,
    SW6 float NULL,
    SW7 float NULL,
    SW8 float NULL,
    SW9 float NULL,
    SW10 float NULL,
    JBM1 float NULL,
    JBM2 float NULL,
    JBM3 float NULL,
    JBM4 float NULL,
    JBM5 float NULL,
    JBM6 float NULL,
    JBM7 float NULL,
    JBM8 float NULL    
)
''' % (dm)
#     sql = '''if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[M5%s]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
# DROP TABLE [dbo].[M5%s]
# ''' % (dm,dm)
    cursor.execute(sql)
    cursor.close()
    db.commit()
#     return
    #最后的日线数据时间
    row = None
#     try:
#         cursor = db.cursor()            
#         sql = "delete FROM M5%s;" % (dm)
#         print sql
#         cursor.execute(sql)
#     except Exception,e:
#         pass
#     cursor.close()
#     db.commit()
#     return
    try:
        cursor = db.cursor()            
        sql = "SELECT max(JYRQ) as JYRQ FROM M5%s;" % (dm)
        cursor.execute(sql)
        row = cursor.fetchone()
    except Exception,e:
        pass
    cursor.close()
    db.commit()
    print 'process: %s' % dm
    f.readline()
    while line:
        t = line.split("\t")
        if len(t) == 8 and t[0] != '      日期':
            try:
                t[0] = "%s %s:%s:00" % (t[0],t[1][0:2],t[1][2:4]) #yyyy-MM-dd HH:mm 
                cjt = datetime.strptime(t[0],"%Y-%m-%d %H:%M:%S")
                if row is not None and row["JYRQ"] is not None:
                    if row["JYRQ"] >= cjt:
                        line = f.readline()
                        continue
                cursor = db.cursor()            
                sql = "insert M5%s (DM,JYRQ,KP,ZG,ZD,SP,CJL,CJE) values('%s','%s',%s,%s,%s,%s,%s,%s);" % (dm,dm,t[0],t[2],t[3],t[4],t[5],t[6],t[7])
                cursor.execute(sql)
                cursor.close()
                db.commit()
            except Exception,e:
                print e
                print '导入数据库错误:',t
        line = f.readline()
    db.close()    
    f.close()
    print '完成一个文件的导入:',fullfilename
    
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
    files = listfilename("/home/wangyi/gp/M5/20150305")
    for file in files:
        filetodb(file)
        