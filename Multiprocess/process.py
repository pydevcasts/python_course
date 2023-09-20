import time
from multiprocessing import Process, current_process
start = time.perf_counter()

def foo(name):
    print(f"Starting with {name}")
    time.sleep(3)
    print(f"Ending with {name}")

f = foo("siyamak")
f = foo("diyana")
end = time.perf_counter()
final = end - start
print(final)
# ====================================

def foo(name):
    print(f"Starting with {name}")
    time.sleep(3)
    print(f"Ending with {name}")

pro1 = Process(target = foo, args=("siyamak",))
pro2 = Process(target = foo, args=("diyana",))
pro1.start()
pro2.start()
pro1.join()
pro1.join()

end = time.perf_counter()
final = end - start
print(final)



