def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    return("Whee!")

say_whee = my_decorator(say_whee)
print(say_whee())
# ==============================================
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee():
#     print("Whee!")
# =============================================
# def auter_uper(func):
#         def bar():
#             return(func().upper())
#         return bar

# def outer_split(func):
#     def inner_split():
#         return func().split(" ")
#     return inner_split

# @outer_split
# @auter_uper
# def moo():
#     """ this is docstrig by moo func"""
#     return("hello siymak ...")
# print(moo())

# ==========================================

# import time
# import math

# def calculate_time(func):
# 	def inner1(*args, **kwargs):
# 		begin = time.time()
# 		func(*args, **kwargs)
# 		end = time.time()
# 		print("Total time taken in : ", func.__name__, end - begin)
# 	return inner1


# @calculate_time
# def factorial(num):
# 	time.sleep(2)
# 	print(math.factorial(num))

# factorial(10)
# =================================
# def hello_decorator(func):
# 	def inner1(*args, **kwargs):
# 		return func(*args, **kwargs)
# 	return inner1


# @hello_decorator
# def sum_two_numbers(a, b):
# 	return a + b

# print("Sum =", sum_two_numbers(1, 2))
# ======================================
# from functools import wraps
# def foo(func):
#     @wraps(func)
#     def outer(*args):
#         """iosdo"""
#         return(func(*args).upper())
#     # outer.__doc__ = func.__doc__
#     return outer

# @foo
# def func_d(name):
#     """this is ariyana"""
#     return(f"hello {name}")
# print(func_d("siyamak"))
# print(func_d.__doc__)
###################################

# import functools
# def foo(v1):
#     def auter_uper(func):
#         @functools.wraps(func)
#         def bar():
#             """this is docstring for test"""
#             return(func().upper())
#         return bar
#     return auter_uper

# @foo("amir")
# def moo():
#     """ this is docstrig by moo func"""
#     return("hello siymak ...")
# print(moo.__name__)
# print(moo.__doc__)

# """
# without functools will got doc and name of obove of func
# """
# ==========================================
