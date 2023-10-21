#ps -e | grep mariadb
#sudo kill -L
#man 7 signal //list signals
import signal  
import time  
import os
# valid_signals = signal.valid_signals()
# print(valid_signals) 



 
# # Our signal handler
# def signal_handler(signum, frame):  
#     print("Signal Number:", signum, " Frame: ", frame)  
 
# def exit_handler(signum, frame):
#     print('Exiting....')
#     exit(0)
 
# # Register our signal handler with `SIGINT`(CTRL + C)
# signal.signal(signal.SIGINT, signal_handler)
 
# # Register the exit handler with `SIGTSTP` (Ctrl + Z)
# signal.signal(signal.SIGTSTP, exit_handler)
 
# # While Loop
# while 1:  
#     print("Press Ctrl + C") 
#     time.sleep(3) 
# ===============================================

import subprocess

# اجرای دستور lsof برای یافتن پردازه‌های مرتبط با پورت 5432
command = "sudo lsof -i :5432"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,\
                        stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    # پردازه‌های مرتبط با پورت 5432 یافت شده‌اند
    # جداگانه هر خط را بررسی کرده و پیدا کرده شده‌ی PID را ببندیم
    lines = result.stdout.split('\n')
    for line in lines:
        if "LISTEN" in line:
            pid = line.split()[1]
            # بستن پردازه با دستور kill
            kill_command = f"sudo kill {pid}"
            subprocess.run(kill_command, shell=True)
        else:
            print("پورت 5432 در حال استفاده نیست.")
else:
    print("هیچ پردازه‌ای برای پورت 5432 یافت نشد یا دسترسی لازم نیست.")
