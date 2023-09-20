import os
from multiprocessing import Process, current_process


def foo(name):
    print(f"Starting with {name}")
    print(os.getpid())  #process id
    print(os.getppid()) #process parent id
    print(f"Ending with {name}")

pro1 = Process(target = foo, args=("siyamak",),name="first")
pro2 = Process(target = foo, args=("diyana",),name = "secund")
pro1.start()
pro2.start()
pro1.join()
pro1.join()