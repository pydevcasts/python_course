import time
from threading import Thread
from concurrent.futures import ProcessPoolExecutor

start = time.perf_counter()

def show(name):
    print(f"Starting {name}")
    time.sleep(3)
    print(f"Ending {name}")


if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        names = ["one", "two", "three", "four"]
        executor.map(show, names) 

    end = time.perf_counter()
    print(end - start)    
