# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:27:29 2023

@author: z1513
"""


def load_mysql(mysql, db,host_input,port_input,user_input,password_input):
    config = {
        'host': host_input
        , 'port': port_input
        , 'user': user_input
        , 'passwd': password_input
        , 'db': db
        , 'use_unicode': True
    }
    conn = py.connect(**config)
    sql_result = pd.read_sql_query(mysql, conn)
    conn.close()
    return sql_result

#修正外呼时间（减一天）
def time_advance(end_time1):
    end_time2=datetime.datetime.strptime(end_time1,'%Y-%m-%d')
    oneday = datetime.timedelta(days=1)
    #明天等于今天减一天
    tomorrow = end_time2 - oneday
    #获取昨天日期的格式化字符串
    end_time = tomorrow.strftime('%Y-%m-%d')
    return end_time
#修正外呼时间（加一天）
def time_delay(end_time1):
    end_time2=datetime.datetime.strptime(end_time1,'%Y-%m-%d')
    oneday = datetime.timedelta(days=1)
    #明天等于今天减一天
    tomorrow = end_time2 + oneday
    #获取昨天日期的格式化字符串
    end_time = tomorrow.strftime('%Y-%m-%d')
    return end_time

def time_adjust_wdhms(time_type,time1,type_wd,days_int,operator):
    time2=datetime.datetime.strptime(time1,time_type)
    if type_wd=='w':
        oneday = datetime.timedelta(weeks=days_int)
    elif type_wd=='h':
        oneday = datetime.timedelta(hours=days_int)
    elif type_wd=='m':
        oneday = datetime.timedelta(minutes=days_int)
    elif type_wd=='s':
        oneday = datetime.timedelta(seconds=days_int)
    else:
        oneday = datetime.timedelta(days=days_int)
    #明天等于今天减一天
    if  operator=='-':
        tomorrow = time2 - oneday
    else:
        tomorrow = time2 + oneday
    #获取昨天日期的格式化字符串
    time = tomorrow.strftime(time_type)
    return time

# 处理外围订单号
def constr(a):
    return str('10') + str(a)