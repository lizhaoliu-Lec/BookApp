import time

def str_to_date(str):
    time = time.mktime(time.strptime(str), '%Y-%m-%d %H:%M:%S')
    t = time.timetuple()
    timeStamp = int(time.m)