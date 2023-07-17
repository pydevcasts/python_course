# x = [1,2,3]
# lister = x.__iter__()
# print(type(lister))
# print(iter(x))
# lister.__next__()
# print(type(lister))
# listitor = lister.__next__()
# print(listitor)
# listitor = lister.__next__()
# print(listitor)
# listitor = lister.__next__()
# print(listitor)

# while True:
#     try:
#         x = lister.__next__()
#         print(x)
#     except StopIteration:
#         break 
# -----------------------------------------------
# class N:
#     def __init__(self, **kwargs):
#         self.dict = {}
    
#     def buy(self, shoes, bag):
#         self.dict[shoes] = self.dict.get(shoes, 0) + bag
    
    # def __iter__(self):
        # print(type(iter(self.dict.items())))
        # return (iter(self.dict.items()))
        
#     def __next__(self):
#         for key, value in self.dict.items():
#             print(key)
#         else:
#             StopIteration


# n = N()
# n.buy('bella', 48)
# n.buy('meli', 46)
# n.buy('nobi', 41)
# n.buy('verda', 14)
# print(next(n))
# for index, staff in n:
    # print(index, staff)
# ---------------------------------------------------------

# class N:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return (self)
        
#     def __next__(self):
#         if self.first >= self.last:
#             raise StopIteration
#         self.first += 1
#         return self.first


# n = N(1, 10)
# for i in n:
#     print(i)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# =============================================

# def foo(start, end):
#     while start <= end:
#         yield start
#         start += 1
# f = foo(1, 10)
# # for i in f:
#     # print(i)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

x = (i for i in range(10))
# print(x.__iter__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
