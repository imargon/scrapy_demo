#-*-coding:UTF-8-*-#
'''
Created on 2015-4-5
当天任务
@author: wangyi
'''

from redline.datainit import di
from redline.fscjdown import fd
from redline.kfscjdown import kfd
from redline.cjmximp import ci
from redline.nextjyrq import nj
from redline.nzfz import nf
from redline.nb import nnb
from redline.fscjeval import fj
from redline.glnzfz import gz
from redline.gleval import ge
from redline.backup import bkd
from redline.dphyfx import dh
from redline.dbhelper import Mysql
from datetime import datetime
from shutil import move

def getPrivDate():
    db = Mysql.getConn()
    cursor = db.cursor()
    sql = '''
        SELECT max(NEXTJYRQ) as JYRQ FROM NEXTJYRQ limit 1;
        '''
    cursor.execute(sql)
    row = cursor.fetchone()
    privdate = row["JYRQ"]
    cursor.close()
    return privdate
def mvdir(currToday):
    cpath = '/home/wangyi/gp/DOWNCJMX/%s' % currToday
    move(cpath,'/home/wangyi/gp/CJMX')
    
if __name__ == '__main__':
    privToday = getPrivDate()
    currToday = datetime.strftime(datetime.now(),'%Y%m%d')
#     currToday = '20150624'
    print '-di-'
    di()
    print 'fd'
    fd(currToday)
    print 'kfd'
    kfd(currToday)
    print 'ci'
    ci(currToday)
    print 'nj'
    nj(currToday)
    print 'nf'
    nf(privToday)
    print 'nb'
    nnb(currToday)
    print 'fj'
    fj(currToday)
    print 'gz'
    gz(privToday)
    print 'ge'
    ge(currToday)
    print 'bk'
    bkd(privToday)
    print 'dh'
    dh(currToday)
    mvdir(currToday)