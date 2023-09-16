"""
time

The epoch is the point where the time starts, the return value of time.gmtime(0).
It is January 1, 1970, 00:00:00 (UTC) on all platforms.
"""

import time


# print(time.time())
# ==================================
# print(time.localtime())
# now = time.localtime()
# print(now.tm_year)
# print(now.tm_mday)
# =================================
# date = time.ctime()
# print(date)
# =================================


# t = time.localtime()
# print(time.mktime(t))

# ===================================
# current_time = time.localtime()
# time_string = time.strftime("%A-%d-%Y %H:%M:%S", current_time)
# print(time_string)
# ========================================

# time_string = "13 Sep 2023"
# result = time.strptime(time_string, "%d %b %Y")
# print(result)
# =========================================

# print("querycode frist")
# time.sleep(2)
# print("querycode secound")
# ========================================
# import random

# while True:
#     print("hello querycode")
#     time.sleep(random.randint(5, 20))


# start = time.time()
# sum = 0
# for i in range(1,100):
#     sum += i
# print(sum)
# print("Run time is:"+str(time.time() - start))
# ================================================


local_time = time.gmtime()
print(local_time)