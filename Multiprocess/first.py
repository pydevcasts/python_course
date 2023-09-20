import os
import time
from multiprocessing import Process, current_process
start = time.perf_counter()

# def foo(name):
#     print(f"Starting with {name}")
#     time.sleep(3)
#     print(f"Ending with {name}")

# f = foo("siyamak")
# f = foo("diyana")
# end = time.perf_counter()
# final = end - start
# print(final)
# ====================================
# def foo(name):
#     print(f"Starting with {name}")
#     time.sleep(3)
#     print(f"Ending with {name}")

# pro1 = Process(target = foo, args=("siyamak",))
# pro2 = Process(target = foo, args=("diyana",))
# pro1.start()
# pro2.start()
# pro1.join()
# pro1.join()

# end = time.perf_counter()
# final = end - start
# print(final)
# ============================================
# def foo(name):
#     print(f"Starting with {name}")
#     print(current_process().name)
#     time.sleep(3)
#     print(f"Ending with {name}")

# pro1 = Process(target = foo, args=("siyamak",),name="first")
# pro2 = Process(target = foo, args=("diyana",),name = "secund")
# pro1.start()
# pro2.start()
# print(pro1.is_alive())
# print(pro2.is_alive())
# pro1.join()
# pro1.join()
# print(pro1.is_alive())
# print(pro2.is_alive())
# end = time.perf_counter()
# print(end - start)
# ===============================================
# def foo(name):
#     print(f"Starting with {name}")
#     print(os.getpid())  #process id
#     print(os.getppid()) #process parent id
#     print(f"Ending with {name}")

# pro1 = Process(target = foo, args=("siyamak",),name="first")
# pro2 = Process(target = foo, args=("diyana",),name = "secund")
# pro1.start()
# pro2.start()
# pro1.join()
# pro1.join()
# ========================================
# def show(name, delay):
#     print(f"Starting with {name} - {delay}")
#     time.sleep(4)
#     print(f"Ending with {name} - {delay}")

# class ShowProcess(Process):
#     def __init__(self, name, delay):
#         super().__init__()
#         self.name = name
#         self.delay = delay

#     def run(self):
#         show(self.name, self.delay)

# process1 = ShowProcess("siyamak", 2)
# process2 = ShowProcess("diyana", 3)
# process1.start()        
# process2.start()         
# process1.join()        
# process2.join()   
# ============================================