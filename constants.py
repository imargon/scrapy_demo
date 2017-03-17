# -*- coding=utf8 -*-
"""
    常量定义
"""
from zhihu.misc.agents import USER_AGENTS

class Gender(object):
    """
    性别定义
    """
    MALE = 1
    FEMALE = 2


class People(object):
    """
    人员类型
    """
    Followee = 1
    Follower = 2


HEADER = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Origin': 'https://www.zhihu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': USER_AGENTS,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    "Upgrade-Insecure-Requests": "1",
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' }

Cookie = {'PAD': '78ede36bfee24204a2fa25a086f523d1||t=1487666563'}
