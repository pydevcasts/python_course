import time
from multiprocessing import Process, current_process

start = time.perf_counter()
def foo(name):
    print(f"Starting with {name}")
    print(current_process().name)
    time.sleep(3)
    print(f"Ending with {name}")

pro1 = Process(target = foo, args=("siyamak",),name="first")
pro2 = Process(target = foo, args=("diyana",),name = "secund")

if __name__ == '__main__':
    pro1.start()
    pro2.start()
    print(pro1.is_alive())
    print(pro2.is_alive())
    pro1.join()
    pro1.join()
    print(pro1.is_alive())
    print(pro2.is_alive())
    end = time.perf_counter()
    print(end - start)
# ===============================================
