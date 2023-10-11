from threading import Timer


def show():
    print("hello siyamak!")

t1 = Timer(3, show)
t2 = Timer(2, show)
t1.start()
t2.start()