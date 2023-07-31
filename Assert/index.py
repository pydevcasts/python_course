# x = 4
# assert x == 5, "x is not equal 5"
# print("x is equal 5")

event = []
def foo(arr):
    assert arr not in event,"event not be repeated"
    event.append(arr)
foo(1)
foo(2)
foo(3)
foo(1)
print(event)

