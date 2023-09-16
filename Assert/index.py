# x = 5
# assert x == 6, "x is not equal 6"

# ==========================================



event = []
def foo(arr):
    assert arr not in event,"arr is in event list"
    event.append(arr)
foo(1)
foo(2)
foo(3)
foo(1)
print(event)

