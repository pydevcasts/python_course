# class N:
#     def __init__(self, name, family):
#         self.name = name
#         self.family = family

#     def foo(self):
#         return f"{self.name}, {self.family}"

# n = N(name="siyamak",family= "abbasi")
# print(n.foo())
# print(n.__dict__)
# ==============================

# class N:
#     _age = 42
#     __name = "mohammad"
#     def foo(self):
#         return self._age, self.__name
# n = N()
# print(n.foo())
# print(N._age)
# print(N.__name__)
# =============================

# class N:
#     def __init__(self, value):
#         self.value = str(value)

#     def __str__(self):
#         return type(self.value)
#     def __float__(self):
#         return type(float(self.value))

# n = N("5")
# print(n.__str__())
# print(n.__float__())
# ===============================
# def foo(arg:int)->str:
#     print(foo.__annotations__)
#     print(foo.__annotations__.get('arg'))
#     print(type(arg))
# foo(10)
# foo("12")

# {'arg': <class 'int'>, 'return': <class 'str'>}
# <class 'int'>
# <class 'int'>
# {'arg': <class 'int'>, 'return': <class 'str'>}
# <class 'int'>
# <class 'str'>
# =================================
# class Base:
#     a: int = 3
#     b: str = 'abc'

# class Derived(Base):
#     print(Base.__annotations__)

# print(Derived.__annotations__)
# ===============================
# from __future__ import annotations
# def foo(a: "str"): 
#     pass

# print(foo.__annotations__)
# ===========================
# class Foo:
#     """
#     name is siyamak
#     """
#     def foo(self):
#         pass
# n = Foo()
# print(n.__doc__)
# =========================

class N():
    def __init__(self, age):
        self.age = age
        
    def foo(self):
        return self.age

    @staticmethod
    def bar(x, y):
        print(x + y)

n = N(5)
n.bar(55,4)
# ==========================

import numpy as np

x = np.array([[1, 1],[2, 2], [3,3]])
print(x[:1])