"""
    输出指定格式的日期。
"""

import time

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime

print(datetime.datetime.today())
print(datetime.date.today())
print(datetime.date.today().strftime('%Y-%m-%d'))
