from multiprocessing import Process
import time


def show(name):
    print(f"Start in {name}...")
    print(f"End in {name}...")
    try:
        1 / 0
    except:
        raise ZeroDivisionError("Error")


p1 = Process(target=show, args=("siyamak",)) 
p2 = Process(target=show, args=("ariana",))

p1.start()
p2.start()

print(p1.is_alive())
print(p2.is_alive())

p1.kill()
p2.terminate()

p1.join()
p2.join()

print(p1.exitcode)
print(p2.exitcode)

print(p1.is_alive())
print(p2.is_alive())