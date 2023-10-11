from threading import Thread, Lock
"""
race condition digit as output undefined
"""
lock = Lock()

num = 0 #shared resource
def add():
    global num
    with lock:
        for _ in range(10000):
            num += 1

def substract():
    global num
    with lock:
        for _ in range(10000):
            num -= 1


p1 = Thread(target=add)
p2 = Thread(target=substract)

p1.start()
p2.start()
p2.join()
p1.join()

print(num)