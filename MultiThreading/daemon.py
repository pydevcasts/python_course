import time
from threading import Thread
import sys

start = time.perf_counter()

def show(name)->str:
    print(f"Starting {name}")
    time.sleep(3)
    print(f"Ending {name}")

thread_one = Thread(target=show, args=("siyamak",),daemon=True)
thread_two = Thread(target=show, args=("azade",), daemon=True)

thread_one.start()
thread_two.start()


end = time.perf_counter()
print(end - start)
sys.exit()
# daemon=True
# اگه برنامه به خط اخر برسه کاری نداره که ترد به 
# پایان رسیده یا نه از برنامه خارج میشه

# daemon=False
# برنامه زمانی به پایان میرسه که ترد کارش تموم بشه