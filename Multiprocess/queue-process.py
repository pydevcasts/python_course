
from multiprocessing import Process,Queue

numbers = []
def foo(queue):
    # global numbers
    nums = queue.get()
    nums.extend([1,2,3])
    queue.put(nums)
    print(nums)

def bar(queue):
    # global numbers
    nums = queue.get()
    nums.extend([3,4,5])
    queue.put(nums)
    print(nums)


qs = Queue()
qs.put(numbers)

f = Process(target=foo, args=(qs,))
b = Process(target=bar, args=(qs,))
f.start()
b.start()
f.join()
b.join()
print(numbers)