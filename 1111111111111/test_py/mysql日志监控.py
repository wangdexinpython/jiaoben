# coding=utf-8
import mysql
import math
import datetime
import time
# from report_common import *
from mysql import connector


# 连接数据库，执行sql语句
def get_data_db(date, hour):
    conn = mysql.connector.connect(host='', user='', passwd='', db='')
    cursor = conn.cursor()
    sql_now = "select '%s','%s',sum(inview_pv),sum(landing_pv)/sum(click) as jiazaiwanchenglv,sum(click)/sum(inview_pv) as dianjilv,sum(download)/sum(click) as kaishixiazailv,sum(downloaded)/sum(click) as xiazaiwancehng,sum(registered)/sum(installed) as jihuowancehnglv from wk_athena_report where date='%s' and hour='%s' group by '%s','%s';" % (
    date, hour, date, hour, date, hour)
    cursor.execute(sql_now)
    now_data = []
    results = cursor.fetchall()
    result = results[0]
    now_data.append(result[2]);
    now_data.append(result[3]);
    now_data.append(result[4]);
    now_data.append(result[6]);
    now_data.append(result[6]);
    now_data.append(result[7]);
    cursor.close()
    conn.commit()
    conn.close()
    return now_data


# 调用函数发送报警信息，如果判断的数据变化幅度大于20%，则认为数据存在异常
def send_email_sms(result=[], result1=[]):
    if abs(result[2] - result1[2]) / result1[2] > 0.2:
        flag = 1
        content = "inview_pv is 20% more than a week ago!"
        req_comm.notice_alarm_mail("实时数据监控", content)
        req_comm.notice_alarm_sms("实时数据监控", content)

    elif abs(result[3] - result1[3]) / result1[3] > 0.2:
        flag = 1
        content = "landing_rate is 20% more than a week ago!"
        req_comm.notice_alarm_mail("实时数据监控", content)
        req_comm.notice_alarm_sms("实时数据监控", content)

    elif abs(result[4] - result1[4]) / result1[4] > 0.2:
        flag = 1
        content = "clicking_rate is 20% more than a week ago!"
        req_comm.notice_alarm_mail("实时数据监控", content)
        req_comm.notice_alarm_sms("实时数据监控", content)

    elif abs(result[5] - result1[5]) / result1[5] > 0.2:
        content = "loading_rate is 20% more than a week ago!"
        flag = 1
        req_comm.notice_alarm_mail("实时数据监控", content)
        req_comm.notice_alarm_sms("实时数据监控", content)

    elif abs(result[6] - result1[6]) / result1[6] > 0.2:
        content = "loaded_rate is 20% more than a week ago!"
        flag = 1
        req_comm.notice_alarm_mail("实时数据监控", content)
        req_comm.notice_alarm_sms("实时数据监控", content)

    elif abs(result[7] - result1[7]) / result1[7] > 0.2:
        content = "register_rate is 20% more than a week ago!"
        flag = 1
        req_comm.notice_alarm_mail("实时数据监控", content)
        req_comm.notice_alarm_sms("实时数据监控", content)


# 设定时间，获取当前时间以及两个小时之前，一天，两天，三天，七天之前的date和hour
if __name__ == "__main__":
    date = time.strftime('%Y-%m-%d')
    now_time = datetime.datetime.now()
    hour = time.strftime("%H")
    hour_int = int(time.strftime("%H"))
    yes_time_0 = now_time + datetime.timedelta(hours=-2)
    hour_2hour_before = int(yes_time_0.strftime("%H"))

    yes_time_00 = now_time + datetime.timedelta(hours=+22)
    hour_22hour_before = int(yes_time_0.strftime("%H"))

    list_1day_before = []
    yes_time_1 = now_time + datetime.timedelta(days=-1)
    date1 = yes_time_1.strftime('%Y-%m-%d')

    list_2day_before = []
    yes_time_2 = now_time + datetime.timedelta(days=-2)
    date2 = yes_time_2.strftime('%Y-%m-%d')

    list_3day_before = []
    yes_time_3 = now_time + datetime.timedelta(days=-3)
    date3 = yes_time_3.strftime('%Y-%m-%d')

    list_7day_before = []
    yes_time_7 = now_time + datetime.timedelta(days=-7)
    date7 = yes_time_7.strftime('%Y-%m-%d')

    list_4day_before = []
    yes_time_4 = now_time + datetime.timedelta(days=-4)
    date4 = yes_time_4.strftime('%Y-%m-%d')

    list_8day_before = []
    yes_time_8 = now_time + datetime.timedelta(days=-8)
    date8 = yes_time_8.strftime('%Y-%m-%d')
    # 判断时间是不是为凌晨2点以后，如果为1点或者是00点，要往前推一天
    if hour_int >= 2:
        list_2hour_before = get_data_db(date, hour_2hour_before)
        list_1day_before = get_data_db(date1, hour_2hour_before)
        list_2day_before = get_data_db(date2, hour_2hour_before)
        list_3day_before = get_data_db(date3, hour_2hour_before)
        list_7day_before = get_data_db(date7, hour_2hour_before)

    else:
        list_2hour_before = get_data_db(date1, hour_22hour_before)
        list_1day_before = get_data_db(date2, hour_22hour_before)
        list_2day_before = get_data_db(date3, hour_22hour_before)
        list_3day_before = get_data_db(date4, hour_22hour_before)
        list_7day_before = get_data_db(date8, hour_22hour_before)
# 根据数据对比情况输出报警信息
#  send_email_sms(list_2hour_before,list_1day_before)
#  send_email_sms(list_2hour_before,list_2day_before)
#  send_email_sms(list_2hour_before,list_3day_before)
#  send_email_sms(list_2hour_before,list_7day_before)