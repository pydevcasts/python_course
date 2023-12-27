import time
from threading import Event, Thread


def first(f,s):
    time.sleep(10)
    print("First is Start...")
    f.set()
    s.wait()
    print("First is working...")

def secund(f,s):
    print("Secund is Start...")
    s.set()
    f.wait()
    print("Secund is working...")

f= Event()
s= Event()
t1 = Thread(target=first, args=(f,s))
t2 = Thread(target=secund, args=(f,s))

t1.start()
t2.start()

