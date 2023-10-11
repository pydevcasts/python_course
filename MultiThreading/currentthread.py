import time
from threading import Thread, current_thread, enumerate

start = time.perf_counter()

def show(name):
    print(f"Starting {name}")
    # print(current_thread().getName())
    # print(current_thread().ident)
    print(enumerate()) #return just alive thread
    time.sleep(3)
    print(f"Ending {name}")

thread_one = Thread(target=show, args=("siyamak",), name="first")
thread_two = Thread(target=show, args=("azade",),name="secund")

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()

end = time.perf_counter()
print(end - start)
