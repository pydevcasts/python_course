from multiprocessing import Process, Lock

def boo(num, lock):
    with lock:
        for _ in range(10000):
            num += 1

def foo(num, lock):
    with lock:
        for _ in range(10000):
            num -= 1

num = 0 #shared resource

lock = Lock()
p1 = Process(target=boo, args=(num,lock))
p2 = Process(target=foo, args=(num,lock))

p1.start()
p2.start()
p2.join()
p1.join()

print(num)