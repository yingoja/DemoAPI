#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import sys, time, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db_fixture.mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-100000))
# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000))

# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event':[
        {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':future_time},
        {'id':2,'name':'苹果iphon6发布会','`limit`':1000,'status':1,'address':'宝安体育馆','start_time':future_time},
        {'id':3,'name':'华为荣耀8发布会','`limit`':2000,'status':0,'address':'深圳福田会展中心','start_time':future_time},
        {'id':4,'name':'苹果iphon8发布会','`limit`':2000,'status':1,'address':'深圳湾体育中心','start_time':past_time},
        {'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','start_time':future_time},
    ],
    #　嘉宾表数据
    'sign_guest':[
        {'id':1,'realname':'Tom','phone':13511886601,'email':'alen@mail.com','sign':0,'event_id':1},
        {'id':2,'realname':'Jason','phone':13511886602,'email':'sign@mail.com','sign':1,'event_id':1},
        {'id':3,'realname':'Jams','phone':13511886603,'email':'tom@mail.com','sign':0,'event_id':5},
    ],
}

# 测试数据插入表
def init_data():
    DB().init_data(datas)
