import sys,time
from multiprocessing import Process


start = time.perf_counter()
def show(name):
    print(f"Starting a process with {name}.....")
    time.sleep(3)
    print(f"Ending a process with {name}.....")


p1 = Process(target = show, args=("siyamak",),daemon=True)
p2 = Process(target = show, args=("diyana",), daemon=True)

p1.start()
p2.start()

end = time.perf_counter()
print(end - start)
sys.exit()

