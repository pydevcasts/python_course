from threading import Thread, RLock
"""
race condition digit as output undefined
"""
lock = RLock()

num = 0 #shared resource
def add():
    global num
    with lock:
        subtract()
        for _ in range(10000):
            num += 1

def subtract():
    global num
    with lock:
        for _ in range(10000):
            num -= 1
def both():
    subtract()
    add()
    
p1 = Thread(target=both)

p1.start()
p1.join()

print(num)