import datetime


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def show(self):
#         print(f"{self.name} is {self.age} years old")

#     @classmethod
#     def birth(cls, name, age):
#         return cls(name, datetime.datetime.now().year - age)


    
# p = Person.birth("siyamak", 1981)
# p.show()
    
# ================================================

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def show(self):
#         print(f"{self.name} is {self.age} years old")

#     @classmethod
#     def birth(cls, name, age):
#         return cls(name, datetime.datetime.now().year - age)

#     @staticmethod
#     def is_adult(age):
#         if age > 35:
#             print("young adoult")
#         else:
#             print("he is teen")

# p = Person.is_adult(42)
# ==========================================
import functools
def foo(v1):
    def auter_uper(func):
        @functools.wraps(func)
        def bar():
            """this is docstring for test"""
            return(func().upper())
        return bar
    return auter_uper

@foo("amir")
def moo():
    """ this is docstrig by moo func"""
    return("hello siymak ...")
print(moo.__name__)
print(moo.__doc__)

"""
without functools will got doc and name of obove of func
"""
# ==========================================