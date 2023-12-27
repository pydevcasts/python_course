import time
from multiprocessing import Pool, cpu_count


def init():
    print("this is initializer")

def foo(name):
    print(f"Starting {name}...")
    time.sleep(3)
    print(f"Ending {name}...")


numes = ["one", "two", "three", "four"]
pool = Pool(processes=cpu_count(), initializer=init)
pool.map(foo, numes)
pool.close()
pool.join()
print(cpu_count())

