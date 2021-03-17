import time
from datetime import datetime
import pytz

def get_chinese_current_date():
    year = time.localtime().tm_year
    #print(year)
    month = time.localtime().tm_mon
    #print(month)
    day = time.localtime().tm_mday
    #print(day)
    return "%s年%s月%s日" %(year,month,day)

def get_english_current_date():
    year = time.localtime().tm_year
    #print(year)
    month = time.localtime().tm_mon
    #print(month)
    day = time.localtime().tm_mday
    #print(day)
    return "%s-%s-%s" %(year,month,day)

def get_chinese_current_time():
    hour = time.localtime().tm_hour
    min = time.localtime().tm_min
    sec = time.localtime().tm_sec
    # print(day)
    return "%s时%s分%s秒" % (hour,min,sec)

def get_english_current_time():
    hour = time.localtime().tm_hour
    min = time.localtime().tm_min
    sec = time.localtime().tm_sec
    # print(day)
    return "%s-%s-%s" % (hour,min,sec)

def get_est_current_time():
    EST = pytz.timezone('US/Eastern')
    year = datetime.now(EST).year
    month = datetime.now(EST).month
    day = datetime.now(EST).day
    hour = datetime.now(EST).hour
    min = datetime.now(EST).minute
    sec = datetime.now(EST).second
    return "%s-%s-%s %s:%s:%s" % (year,month,day,hour,min,sec)

def get_chinese_datetime():
    return get_chinese_current_date()+get_chinese_current_time()

def get_english_datetime():
    return get_english_current_date()+" "+get_english_current_time()

def get_cur_hour():
    return time.localtime().tm_hour


if __name__ == "__main__":
    print(get_chinese_current_date())
    print(get_english_current_date())
    print(get_chinese_current_time())
    print(get_english_current_time())
    print(get_chinese_datetime())
    print(get_english_datetime())
    print(get_est_current_time())
