# -*- coding: utf-8 -*- 
'''
Created on 2015-3-15

@author: wangyi
'''
import numpy as np
import time
import math

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
c = np.loadtxt("/home/wangyi/gp/CJMX/201504/20150421/20150421-601377.txt",delimiter='\t', skiprows=1,converters={0:bstimetosn,5:bstonum}, usecols=(0,1,2,3,4,5), unpack=False)
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
print 'bze,bzl,sze,szl,pjbj,pjsj,pjjbz,pjjcz'
print bze,bzl,sze,szl,pjbj,pjsj,pjjbz,pjjcz
print '-------------------------------------------'
pjbl = np.mean(c[c[...,5]>0][...,3])
pjsl = np.mean(c[c[...,5]<0][...,3])
pjlbz = pjbl/ pjsl
pjlcz = pjbl - pjsl
# print 'pjbl,pjsl,pjlbz,pjlcz'
# print pjbl,pjsl,pjlbz,pjlcz
# print '-------------------------------------------'
zxpl = np.sum(c[c[...,5]==0][...,3])
zxpe = np.sum(c[c[...,5]==0][...,4])
zxpbz = zxpl/(zxpl + bzl + szl)
fzxpbz = 1.0 - zxpbz
zxpebz = zxpe/(zxpe + bze + sze)
# print 'zxpl,zxpbz,fzxpbz,zxpe,zxpebz'
# print zxpl,zxpbz,fzxpbz,zxpe,zxpe/(zxpe + bze + sze)
# print '-------------------------------------------'
 
ptp = np.ptp(c[...,1])
min = np.min(c[...,1])
h= ptp * 0.618
h= h + min
m= ptp * 0.382
m = m + min
# print 'h,m'
# print h,m
# print '---------------------------------------'
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
 
 
# print 'gjbdl,gjbdj,gjfsb,gjfsb/daysecond,gjbdl/(zxpl + bzl + szl),gjbde,gjbde/(zxpe + bze + sze)'
# print gjbdl,gjbdj,gjbdfs,gjbdfs/daysecond,gjbdl/(zxpl + bzl + szl),gjbde,gjbde/(zxpe + bze + sze)
# print 'gjsdl,gjsdj,gjfss,gjfss/daysecond,gjsdl/(zxpl + bzl + szl),gjsde,gjsde/(zxpe + bze + sze)'
# print gjsdl,gjsdj,gjsdfs,gjsdfs/daysecond,gjsdl/(zxpl + bzl + szl),gjsde,gjsde/(zxpe + bze + sze)
# print '---------------------------------------------------------'
 
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
 
# print 'zjbdl,zjbdj,zjfsb,zjfsb/daysecond,zjbde,zjbdl/(zxpl + bzl + szl),zjbde/(zxpe + bze + sze)'
# print zjbdl,zjbdj,zjbdfs,zjbdfs/daysecond,zjbde,zjbdl/(zxpl + bzl + szl),zjbde/(zxpe + bze + sze)
# print 'zjsdl,zjsdj,zjfss,zjfss/daysecond,zjsde,zjsdl/(zxpl + bzl + szl),zjsde/(zxpe + bze + sze)'
# print zjsdl,zjsdj,zjsdfs,zjsdfs/daysecond,zjsde,zjsdl/(zxpl + bzl + szl),zjsde/(zxpe + bze + sze)
# print '---------------------------------------'
 
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
 
# print 'djbdl,djbdj,djfsb,djfsb/daysecond,djbde,djbdl/(zxpl + bzl + szl),djbde/(zxpe + bze + sze)'
# print djbdl,djbdj,djbdfs,djbdfs/daysecond,djbde,djbdl/(zxpl + bzl + szl),djbde/(zxpe + bze + sze)
# print 'djsdl,djsdj,djfss,djfss/daysecond,djsde,djsdl/(zxpl + bzl + szl),djsde/(zxpe + bze + sze)'
# print djsdl,djsdj,djsdfs,djsdfs/daysecond,djsde,djsdl/(zxpl + bzl + szl),djsde/(zxpe + bze + sze)
# print '---------------------------------'
 
lh = (pjbl + pjsl) * 0.618
lm = (pjbl + pjsl) * 0.382
# print 'lh,lm'
# print lh,lm
# print '---------------------------------------'
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
 
# print 'glbdl,glbdj,glfsb,glfsb/daysecond,glbdl/(zxpl + bzl + szl),glbde,glbde/(zxpe + bze + sze)'
# print glbdl,glbdj,glbdfs,glbdfs/daysecond,glbdl/(zxpl + bzl + szl),glbde,glbde/(zxpe + bze + sze)
# print 'glsdl,glsdj,glfss,glfss/daysecond,glsdl/(zxpl + bzl + szl),glsde,glsde/(zxpe + bze + sze)'
# print glsdl,glsdj,glsdfs,glsdfs/daysecond,glsdl/(zxpl + bzl + szl),glsde,glsde/(zxpe + bze + sze)
# print '---------------------------------------------------------'
 
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
# print 'zlbdl,zlbdj,zlfsb,zlfsb/daysecond,zlbde,zlbdl/(zxpl + bzl + szl),zlbde/(zxpe + bze + sze)'
# print zlbdl,zlbdj,zlfsb,zlfsb/daysecond,zlbde,zlbdl/(zxpl + bzl + szl),zlbde/(zxpe + bze + sze)
# print 'zlsdl,zlsdj,zlfss,zlfss/daysecond,zlsde,zlsdl/(zxpl + bzl + szl),zlsde/(zxpe + bze + sze)'
# print zlsdl,zlsdj,zlfss,zlfss/daysecond,zlsde,zlsdl/(zxpl + bzl + szl),zlsde/(zxpe + bze + sze)
# print '---------------------------------------'
 
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
 
zs = c[0,1] + c[0,2]
print 'zs',zs
jk = c[0,1]
print 'jk',jk
zg = np.max(c[...,1])
print 'zg',zg
zd = np.min(c[...,1])
print 'zd',zd
zf = np.sum(c[...,2])
print 'zf',zf
zfz = zf/zs * 100
print 'zfz',zfz
 
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
 
print zxpebz + gjbdebz + gjsdebz + zjbdebz + zjsdebz + djbdebz + djsdebz
print zxpebz + glbdebz + glsdebz + zlbdebz + zlsdebz + dlbdebz + dlsdebz
 
dyjgl =  np.sum(c[c[...,2]<0][...,3])
dycs = np.count_nonzero(c[c[...,2]<0][...,3])
dyjl = np.mean(c[c[...,2]<0][...,3])
dymax = np.max(c[c[...,2]<0][...,2])
tsjgl =  np.sum(c[c[...,2]>0][...,3])
tscs =  np.count_nonzero(c[c[...,2]>0][...,3])
tsjl = np.mean(c[c[...,2]>0][...,3])
tsmax = np.max(c[c[...,2]>0][...,2])
dyjgfd =  np.sum(c[c[...,2]<0][...,2])
tsjgfd =  np.sum(c[c[...,2]>0][...,2])
dylbz = dyjgl / (bzl + szl + zxpl)
tslbz = tsjgl / (bzl + szl + zxpl)
mdy = dyjgl / (np.fabs(dyjgfd) * 100)
mts = tsjgl / (tsjgfd * 100)
print '打压价格和抬升价格量:',dyjgl,tsjgl
print '打压价格空间和抬升价格空间:',dyjgfd,tsjgfd
print dylbz,tslbz ,(bzl + szl + zxpl)
print mdy,mts,
mcz = mts - mdy
print mcz
print dycs,tscs,dymax,tsmax,dyjl,tsjl
 
tszdl = np.max(c[c[...,2]==tsmax][...,3])
print tszdl
dyzdl = np.max(c[c[...,2]< 0][...,3])
print dyzdl
zdzl = (tsjgl - dyjgl) / ((tsjgfd + dyjgfd) * 100)
print zdzl
 
zjlc = np.sum(c[c[...,2]< 0][...,3] * c[c[...,2]< 0][...,1] * 100)
zjlr = np.sum(c[c[...,2]> 0][...,3] * c[c[...,2]> 0][...,1] * 100)
 
print zjlc  - zjlr 
 
 
# print 'dlbdl,dlbdj,dlfsb,dlfsb/daysecond,dlbde,dlbdl/(zxpl + bzl + szl),dlbde/(zxpe + bze + sze)'
# print dlbdl,dlbdj,dlfsb,dlfsb/daysecond,dlbde,dlbdl/(zxpl + bzl + szl),dlbde/(zxpe + bze + sze)
# print 'dlsdl,dlsdj,dlfss,dlfss/daysecond,dlsde,dlsdl/(zxpl + bzl + szl),dlsde/(zxpe + bze + sze)'
# print dlsdl,dlsdj,dlfss,dlfss/daysecond,dlsde,djsdl/(zxpl + bzl + szl),dlsde/(zxpe + bze + sze)
# print '---------------------------------'
 
# print 0.0107712305541 + 0.0343362941244 + 0 + 0.0454103555706 + 0.0165112039182 + 0.424730252285 + 0.468240663548
# print 0.0107712305541 + 0.286024109847 + 0.179998019849 + 0.15627550842 +0.172417768942 + 0.0621772837134 +0.132336078676 
 
print '0930',bstimetosn('09:30:03')
print '0945',bstimetosn('09:45:03')
print '1130',bstimetosn('11:30:03')
print '1315',bstimetosn('13:15:03')
print '1500',bstimetosn('15:00:03')
 
print '0930-0945' ,bstimetosn('09:30:03')-bstimetosn('09:45:03')
 
print '1130-1315',bstimetosn('11:30:03')-bstimetosn('13:15:03')
bs = int(bstimetosn("09:30:00"))
es = int(bstimetosn('15:00:00'))
# for i in range(bs,es,60):
#     try:
#         tn = c[c[...,6] < i]
#         if i  > 1420075853:
#             j = i -60
#             tn = tn[tn[...,6] > j]
# #         print tn 
#         try:
#             dyjgl =  np.sum(tn[tn[...,2]<0][...,3])
#         except:
#             dyjgl = 0
#         try:
#             dycs = np.count_nonzero(tn[tn[...,2]<0][...,3])
#         except:
#             dycs =0
#         try:
#             dyjl = np.mean(tn[tn[...,2]<0][...,3])
#         except:
#             dyjl =0
#         try:
#             dymax = np.max(tn[tn[...,2]<0][...,2])
#         except:
#             dymax = 0
#         try:
#             tsjgl =  np.sum(tn[tn[...,2]>0][...,3])
#         except:
#             tsjgl = 0
#         try:
#             tscs =  np.count_nonzero(tn[tn[...,2]>0][...,3])
#         except:
#             tscs = 0
#         try:
#             tsjl = np.mean(tn[tn[...,2]>0][...,3])
#         except:
#             tsjl = 0
#         
#         try:
#             tsmax = np.max(tn[tn[...,2]>0][...,2])
#         except:
#             tsmax = 0
#         
#         try:
#             dyjgfd =  np.sum(tn[tn[...,2]<0][...,2])
#         except:
#             dyjgfd = 0
#         try:
#             tsjgfd =  np.sum(tn[tn[...,2]>0][...,2])
#         except:
#             tsjgfd = 0
#         dylbz = dyjgl / (bzl + szl + zxpl)
#         tslbz = tsjgl / (bzl + szl + zxpl)
#         mdy = dyjgl / (np.fabs(dyjgfd) * 100)
#         mts = tsjgl / (tsjgfd * 100)
#         print '打压价格和抬升价格量:',dyjgl,tsjgl
#         print '打压价格空间和抬升价格空间:',dyjgfd,tsjgfd
#         print "dylbz,tslbz ,(bzl + szl + zxpl)"
#         print dylbz,tslbz ,(bzl + szl + zxpl)
#         print "每分钱打压和抬升量平均"
#         print mdy,mts,
#         mcz = mts - mdy
#         print "打压抬升差"
#         print mcz
#         print "打压次数,抬升次数,最大打压,最小打压,平均每次打压量,平均每次抬升量"
#         print dycs,tscs,dymax,tsmax,dyjl,tsjl
#         try:
#             tszdl = np.max(tn[tn[...,2]==tsmax][...,3])
#         except:
#             tszdl =0
#         print tszdl
#         try:
#             dyzdl = np.max(tn[tn[...,2]< 0][...,3])
#         except:
#             dyzdl =0
#         
#         print dyzdl
#         zdzl = (tsjgl - dyjgl) / ((tsjgfd + dyjgfd) * 100)
#         print zdzl
#         try:
#             zjlc = np.sum(tn[tn[...,2]< 0][...,3] * tn[tn[...,2]< 0][...,1] * 100)
#         except:
#             zjlc =0
#         try:
#             zjlr = np.sum(tn[tn[...,2]> 0][...,3] * tn[tn[...,2]> 0][...,1] * 100)
#         except:
#             zjlr =0
#         print zjlc  - zjlr 
#     except Exception,e:
#         print e
# for i in range(bs,es,60):
#     try:
#         tn = c[c[...,6] <= i]
#         ib = i -60
#         tn = tn[tn[...,6] > ib]
#         print (i - bs) / 60 + 1
# #         if i  > 1420075853:
# #             j = i -60
# #             tn = tn[tn[...,6] > j]
#         try:
#             print 'price',tn[-1,1]
#             print 'jf',np.sum(tn[...,2])
#             print tn[...,2]
#             print np.sum(tn[tn[...,5]< 0][...,0])
#             print np.sum(tn[tn[...,5]< 0][...,3])
#             print np.sum(tn[tn[...,2]< 0][...,2])
#             print np.sum(tn[tn[...,2]< 0][...,0])
#             if np.sum(tn[tn[...,5]< 0][...,3]) == 0 or np.sum(tn[tn[...,5]< 0][...,0])==0 :
#                 dysd = 0
#             else :
#                 dysd = np.sum(tn[tn[...,5]< 0][...,3]) / np.sum(tn[tn[...,5]< 0][...,0])
#             if np.sum(tn[tn[...,2]< 0][...,2]) == 0 or np.sum(tn[tn[...,2]< 0][...,0])==0:
#                 dysd1 = 0
#             else:
#                 dysd1 = np.sum(tn[tn[...,2]< 0][...,2]) / np.sum(tn[tn[...,2]< 0][...,0])
#               
#         except:
#             dysd = 0
#             dysd1 = 0
#         try: 
#             if np.sum(tn[tn[...,5]> 0][...,3]) == 0 or np.sum(tn[tn[...,5]> 0][...,0])==0:
#                 tssd = 0
#             else:  
#                 tssd = np.sum(tn[tn[...,5]> 0][...,3]) / np.sum(tn[tn[...,5]> 0][...,0])
#             if np.sum(tn[tn[...,2]> 0][...,2]) == 0 or np.sum(tn[tn[...,2]> 0][...,0])==0:
#                 tssd1 = 0
#             else:
#                 tssd1 = np.sum(tn[tn[...,2]> 0][...,2]) / np.sum(tn[tn[...,2]> 0][...,0])
#         except:
#             tssd = 0
#             tssd1 = 0
#         print "dysd,dysd1,tssd,tssd1,he\n"
#         print dysd,dysd1,tssd,tssd1, dysd * dysd1 + tssd * tssd1,"\n"
#     except:
#         pass
#         
#         
# print int(bstimetosn("09:30:00"))
