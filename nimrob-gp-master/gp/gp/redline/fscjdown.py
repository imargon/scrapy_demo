#-*-coding:UTF-8-*-#
'''
Created on 2015-3-11

@author: wangyi
'''

#DownByDate.py sh600115 2014-12-29 2015-3-15
#DownByDate.py stock_num start_date end_date
 
#http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c=sh600115&d=20141229
#sh600115_2014-12-29.txt
 
import sys
import urllib
import datetime
import os
import os.path
import time
import socket
socket.setdefaulttimeout(20)

def listfilename(rootdir):
    fullfilename = []
    for parent,dirnames,filenames in os.walk(rootdir):  
#     for dirname in  dirnames:                      
#         print "parent is:" + parent
#         print  "dirname is" + dirname
#     print 'files:'
    
        for filename in filenames:                       
    #         print "parent is" + parent
    #         print "filename is:" + filename
             fullfilename.append(os.path.join(parent,filename)) 
    return fullfilename
def listdirname(rootdir):
    fullfilename = []
    for parent,dirnames,filenames in os.walk(rootdir):  
        for dirname in  dirnames:                      
#             print "parent is:" + parent
#             print  "dirname is" + dirname
            fullfilename.append(os.path.join(parent,dirname))
#     print 'files:'
    
#         for filename in filenames:                       
#     #         print "parent is" + parent
#     #         print "filename is:" + filename
#              fullfilename.append(os.path.join(parent,filename)) 
    return fullfilename 
def download_date(src_url,dest_file):
    download=urllib.FancyURLopener();
    download_page=download.open(src_url);
    savefile=file(dest_file,'wb+');
    while True:
        arr = download_page.read();
        if len(arr)==0:
            break;
        savefile.write(arr);
    savefile.flush();
    savefile.close();
    return
#http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c=sh002039&d=20150303#sh002039_2015-03-03.txt 
# stock_code=sys.argv[1]
# str_0='''http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c='''
# str_0=str_0 + stock_code + '&d='
# date_start=datetime.datetime.strptime(sys.argv[2],'%Y-%m-%d')
# if len(sys.argv)>3:
#     date_end=datetime.datetime.strptime(sys.argv[3],'%Y-%m-%d')
# else:
#     date_end=date_start+datetime.timedelta(days=1)

str_url = "http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c=%s&d=%s#%s_%s.txt" 

def fd(currToday):
    files = listfilename("/mnt/windows/gp/D1/ZZX")
    cpath = '/home/wangyi/gp/DOWNCJMX/%s' % currToday
    os.mkdir(cpath)
    for filen in files:
        str_date = listdirname('/home/wangyi/gp/DOWNCJMX')
        for dirname in str_date:
            ddt = dirname[-8:]
            fmddt = ddt
            ddt = "%s-%s-%s" % (ddt[0:4],ddt[4:6],ddt[6:8])         
            gpdm = filen[-12:-4].lower() #锟斤拷票锟斤拷锟斤拷锟饺�
            dm = filen[-10:-4]
            url =  str_url % (gpdm,fmddt,gpdm,ddt)
            dest_file = "%s/%s-%s.txt" % (dirname,fmddt,dm)
            try:
                download_date(url,dest_file)
            except Exception,e:
                print e
            print 'down a file: %s' % dest_file

if __name__ == '__main__':
#     files = listfilename("d:\\gp\\002297")
#     print files
#     print files[0]
#     print files[0][-10:-4]
#     d = files[0][-19:-11]
#     print d
#     fd = "%s-%s-%s" % (d[0:4],d[4:6],d[6:8])
#     print fd
    files = listfilename("/mnt/windows/gp/D1/ZZX")

    for filen in files:
        str_date = listdirname('/home/wangyi/gp/DOWNCJMX')
        
        for dirname in str_date:
            ddt = dirname[-8:]
            fmddt = ddt
            ddt = "%s-%s-%s" % (ddt[0:4],ddt[4:6],ddt[6:8])         
            gpdm = filen[-12:-4].lower() #锟斤拷票锟斤拷锟斤拷锟饺�
            dm = filen[-10:-4]
#             print len(ddt)
#             print fmddt
#             print ddt
#             print gpdm
#             break
            url =  str_url % (gpdm,fmddt,gpdm,ddt)
#             print url
            dest_file = "%s/%s-%s.txt" % (dirname,fmddt,dm)
#             print dest_fileu
#             print dm
#             break
            try:
                download_date(url,dest_file)
            except Exception,e:
                print e
            print 'down a file: %s' % dest_file
#             time.sleep(0.5)
        
# while date_start<date_end: 
#     str_date="date_start.strftime('%Y%02m%02d')" 
#     str_url="str_0+str_date" 
#     str_file="stock_code=" + "sz002039"  
#     date_start.strftime("%y-%02m-%02d")=""
#     download_date(str_url,str_file)
#     print date_start "date_start+datetime.timedelta(days=1)

