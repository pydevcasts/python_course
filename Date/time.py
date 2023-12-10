import time
seconds = time.time()
print("Current time in seconds since epoch =", seconds)

# OUTPUT
# Current time in seconds since epoch = 1582961644.3032079
########################################################
import time
 
print("JournalDev!!!!.")
time.sleep(1.2)
print("AskPython.")
time.sleep(3.2)
print("Engineering")
# OUTPUT

# JournalDev!!!!.
# AskPython.
# Engineering/
############################################################
import time
 
local_time = time.localtime()
print("Time:",local_time)
print("Current year:", local_time.tm_year)
print("Current hour:", local_time.tm_hour)
print("Current minute:", local_time.tm_min)
print("Current second:", local_time.tm_sec)


# OUTPUT
# Time: time.struct_time(tm_year=2020, tm_mon=2, tm_mday=29, tm_hour=14, tm_min=3, tm_sec=23, tm_wday=5, tm_yday=60, tm_isdst=0)
# Current year: 2020
# Current hour: 14
# Current minute: 3
# Current second: 23
##########################################################
from time import time, ctime
 
current_time = time()
res = ctime(time)
print("Local_time:",res)

# OUTPUT
# Local_time: Sat Feb 29 14:08:26 2020
# متد time.ctime () مقدار ثانیه را از نتیجه فانکشن time() به عنوان یک آرگومان می گیرد و یک مقدار رشته را نشان می دهد
# که نشان دهنده زمان محلی فعلی است.
########################################################
import time
 
local_time = time.localtime()
sec = time.mktime(local_time)
print(sec)


# OUTPUT
# 1582966721.0
#  زمان را در ثانیه ای که از دوران گذشته سپری شده است
#############################################
import time
 
local_time = time.gmtime()
print(local_time)


# OUTPUT
# time.struct_time(tm_year=2020, tm_mon=2, tm_mday=29, tm_hour=9, tm_min=2, tm_sec=49, tm_wday=5, tm_yday=60, tm_isdst=0)
# زمان فعلی را در قالب کلاس struct_time در UTC باز می گرداند.
#################################################

import time
 
tym = "29 February, 2020"
sys = time.strptime(tym, "%d %B, %Y")
print(sys)

# OUTPUT
# time.struct_time(tm_year=2020, tm_mon=2, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=60, tm_isdst=-1)
#  زمان را در قالب struct_time برمی گرداند
#########################################################
import time
 
tym = time.localtime()
opt = time.strftime("%d/%m/%Y, %H:%M:%S",tym)
 
print(opt)


# OUTPUT
# 29/02/2020, 15:07:16
#  زمان را با توجه به کدهای قالب ورودی نشان می دهد.
#######################################################
import time
 
tym = time.localtime()
 
opt = time.asctime(tym)
print("TimeStamp:",opt)


# OUTPUT
# TimeStamp: Sat Feb 29 15:27:14 2020
# که ورودی زمان را از چندتایی کلاس 
# struct_time
# نشان می دهد.