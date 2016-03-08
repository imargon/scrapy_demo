#-*-coding:UTF-8-*-#
'''
Created on 2015-3-6

@author: wangyi
'''
from redline.dbhelper import Mysql

import os
import os.path
import sys


currdate = ''

def listfilename(rootdir):
    fullfilename = []
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     for dirname in  dirnames:                       #输出文件夹信息
#         print "parent is:" + parent
#         print  "dirname is" + dirname
#     print 'files:'
    
        for filename in filenames:                        #输出文件信息
    #         print "parent is" + parent
             print "filename is:" + filename
             fullfilename.append(os.path.join(parent,filename)) #输出文件路径信息
    return fullfilename

'''a file to database'''

def filetodb(fullfilename):
    tf = fullfilename[-5:-4] #文件名称
    if tf == '1':
        hsag1(fullfilename)
    elif tf== '2':
        hsag2(fullfilename)
    elif tf== '3':
        hsag3(fullfilename)
    elif tf== '4':
        hsag4(fullfilename)
    elif tf== '5':
        hsag5(fullfilename)
   
#沪深A股表1导入处理
def hsag1(fullfilename):
    f = open(fullfilename)
    line = f.readline()
    db = Mysql.getConn()#获取池中连接
    try:
        cursor = db.cursor()            
        sql = "delete FROM HSAG WHERE JYRQ='%s';" % (currdate)
        print sql
        cursor.execute(sql)
    except Exception,e:
        pass
    cursor.close()
    db.commit()
    while line:
        t = line.split("\t")
        if len(t) == 25 and t[0].decode("gbk").encode("utf8") != '代码':
            try:
                for i in range(0,24):
                    t[i] = t[i].decode("gbk").encode("utf8")
                    if t[i] == '--  ':
                        t[i] = 0
#                     if i == 1 or i==18 or i==19 :
#                         t[i] = t[i].encode('gb2312')
                cursor = db.cursor()            
                sql = '''
        INSERT HSAG 
        (
            DM,MC,JYRQ,ZF,XJ,JD,BJ,SJ,ZL,
            XL,ZS,HS,JK,ZG,ZD,
            ZTS,SYD,ZJE,LB,XFHY,DQ,
            ZFL,JJ,NP,WP
        )
        VALUES 
        (    
            '%s','%s','%s',%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,'%s','%s',
            %s,%s,%s,%s
        )
                ''' % (t[0],
                       t[1],currdate,t[2],t[3],t[4],t[5],t[6],t[7],
                       t[8],t[9],t[10],t[11],t[12],t[13],
                       t[14],t[15],t[16],t[17],t[18],t[19],
                       t[20],t[21],t[22],t[23]
                       )
#                 print sql
#                 sql = sql.encode("utf8")
#                 print sql 
                cursor.execute(sql)
                cursor.close()
                db.commit()
            except Exception,e:
                print '导入数据库错误:'
                print e
    
        line = f.readline()
    db.close()    
    f.close()
    print '完成一个文件的导入:',fullfilename

#沪深A股表2导入处理
def hsag2(fullfilename):
    f = open(fullfilename)
    line = f.readline()
    db = Mysql.getConn()#获取池中连接

    while line:
        t = line.split("\t")
        if len(t) == 21 and t[0].decode("gbk").encode("utf8") != '代码':
            try:
                for i in range(0,20):
                    t[i] = t[i].decode("gbk").encode("utf8")
                    if t[i] == '--  ':
                        t[i] = 0
                    if i == 7:
                        t[i] = t[i][:-3]
                    if i == 8:
                        t[i] = t[i][:-3]
                cursor = db.cursor()            
                sql = '''

        UPDATE HSAG 
        SET MC='%s',NWB=%s,MRL=%s,MCL=%s,WPPL=%s,LTGB=%s,LTSJ=%s,
            ABGZSJ=%s,QYD=%s,HYD=%s,MBJL=%s,MBHS=%s,CWGX='%s',
            SSRQ='%s',ZGB=%s,BG=%s,HG=%s,ZZC=%s,JZC=%s
        WHERE DM='%s' AND JYRQ='%s'
                ''' % (
                       t[1],t[2],t[3],t[4],t[5],t[6],t[7],
                       t[8],t[9],t[10],t[11],t[12],t[13],
                       t[14],t[15],t[16],t[17],t[18],t[19],
                       t[0],currdate
                       )
#                 print sql
#                 sql = sql.encode("utf8")
#                 print sql 
                cursor.execute(sql)
                cursor.close()
                db.commit()
            except Exception,e:
                print '导入数据库错误:'
                print e
    
        line = f.readline()
    db.close()    
    f.close()
    print '完成一个文件的导入:',fullfilename

#沪深A股表3导入处理
def hsag3(fullfilename):
    f = open(fullfilename)
    line = f.readline()
    db = Mysql.getConn()#获取池中连接

    while line:
        t = line.split("\t")
        if len(t) == 17 and t[0].decode("gbk").encode("utf8") != '代码':
            try:
                for i in range(0,16):
                    t[i] = t[i].decode("gbk").encode("utf8")
                    if t[i] == '--  ':
                        t[i] = 0
                cursor = db.cursor()            
                sql = '''
        UPDATE HSAG 
        SET MC='%s',XSGQ=%s,ZCHZL=%s,LDZC=%s,GDZC=%s,WXZC=%s,LDHZ=%s,
            GJJ=%s,CH=%s,YSZK=%s,YYSR=%s,YYCB=%s,YYLR=%s,
            TZSY=%s,LRZE=%s
        WHERE DM='%s' AND JYRQ='%s'

                ''' % (
                       t[1],t[2],t[3],t[4],t[5],t[6],t[7],
                       t[8],t[9],t[10],t[11],t[12],t[13],
                       t[14],t[15],
                       t[0],currdate                       
                       )
#                 sql = sql.encode("utf8")
                cursor.execute(sql)
                cursor.close()
                db.commit()
            except Exception,e:
                print '导入数据库错误:'
                print e
    
        line = f.readline()
    db.close()    
    f.close()
    print '完成一个文件的导入:',fullfilename


#沪深A股表4导入处理
def hsag4(fullfilename):
    f = open(fullfilename)
    line = f.readline()
    db = Mysql.getConn()#获取池中连接

    while line:
        t = line.split("\t")
        if len(t) == 19 and t[0].decode("gbk").encode("utf8") != '代码':
            try:
                for i in range(0,17):
                    t[i] = t[i].decode("gbk").encode("utf8")
                    if t[i] == '--  ':
                        t[i] = 0
                    if i == 15:
                        t[i] = t[i][:-3]
                    if i == 9:
                        t[i] = t[i][:-3]
                cursor = db.cursor()            
                sql = '''
        UPDATE HSAG 
        SET MC='%s',SHLR=%s,JLR=%s,WFLR=%s,JYXJL=%s,ZXJL=%s,GDRS=%s,
            RJCG=%s,RJSJ=%s,LRTB=%s,SRTB=%s,SZL=%s,SXL=%s,
            SXLT=%s,MGSY=%s,MGJZ=%s,TZHJZ=%s
        WHERE DM='%s' AND JYRQ='%s'
        ''' % (
                       t[1],t[2],t[3],t[4],t[5],t[6],t[7],
                       t[8],t[9],t[10],t[11],t[12],t[13],
                       t[14],t[15],t[16],t[17],
                       t[0],currdate        
                       )
#                 sql = sql.encode("utf8")
#                 print sql
                cursor.execute(sql)
                cursor.close()
                db.commit()
            except Exception,e:
                print '导入数据库错误:'
                print e
    
        line = f.readline()
    db.close()    
    f.close()
    print '完成一个文件的导入:',fullfilename

#沪深A股表5导入处理
def hsag5(fullfilename):
    f = open(fullfilename)
    line = f.readline()
    db = Mysql.getConn()#获取池中连接

    while line:
        t = line.split("\t")
        if len(t) == 14 and t[0].decode("gbk").encode("utf8") != '代码':
            try:
                jd =''
                for i in range(0,13):
                    t[i] = t[i].decode("gbk").encode("utf8")
                    if t[i] == '--  ':
                        t[i] = 0
                    if i == 5:
                        jd = t[i][-3:]
#                         print jd
                        t[i] = t[i][:-3]
#                         print t[i]
                cursor = db.cursor()            
                sql = '''
        UPDATE HSAG 
        SET MC='%s',MGGJ=%s,MGWFP=%s,QYB=%s,ZYL=%s,ZYLJD='%s',SSMLL=%s,YYLRL=%s,
        JLRL=%s,JYDM='%s',LASTDATE=now()
        WHERE DM='%s' AND JYRQ='%s'
      ''' % (
                       t[1],t[2],t[3],t[4],t[5],jd,t[6],t[7],
                       t[8],t[9],
                       t[0],currdate                       
                       )
#                 print sql
#                 sql = sql.encode("utf8")
                
                cursor.execute(sql)
                cursor.close()
                db.commit()
            except Exception,e:
                print '导入数据库错误:'
                print e
    
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
#     files = listfilename("/mnt/windows/gp/HSAG/20150320")
#     print files
#     
#     for file in files:
# #         print file
#         currdate = file[-18:-10]
# #         print currdate;
#         filetodb(file)
    dstr = "/mnt/windows/gp/HSAG/20150504/"
    currdate = dstr[-9:-1]

    hsag1(dstr + "HSAG1.txt");
    hsag2(dstr + "HSAG2.txt");
    hsag3(dstr + "HSAG3.txt");
    hsag4(dstr + "HSAG4.txt");
    hsag5(dstr + "HSAG5.txt");
     