# # class N:
# #     def __init__(self, name, family):
# #         self.name = name
# #         self.family = family

# #     def foo(self):
# #         return f"{self.name}, {self.family}"

# # n = N(name="siyamak",family= "abbasi")
# # print(n.foo())
# # print(n.__dict__)
# # ==============================

# # class N:
# #     _age = 42
# #     __name = "mohammad"
# #     def foo(self):
# #         return self._age, self.__name
# # n = N()
# # print(n.foo())
# # print(N._age)
# # print(N.__name__)
# # =============================

# # class N:
# #     def __init__(self, value):
# #         self.value = str(value)

# #     def __str__(self):
# #         return type(self.value)
# #     def __float__(self):
# #         return type(float(self.value))

# # n = N("5")
# # print(n.__str__())
# # print(n.__float__())
# # ===============================
# # def foo(arg:int)->str:
# #     print(foo.__annotations__)
# #     print(foo.__annotations__.get('arg'))
# #     print(type(arg))
# # foo(10)
# # foo("12")

# # {'arg': <class 'int'>, 'return': <class 'str'>}
# # <class 'int'>
# # <class 'int'>
# # {'arg': <class 'int'>, 'return': <class 'str'>}
# # <class 'int'>
# # <class 'str'>
# # =================================
# # class Base:
# #     a: int = 3
# #     b: str = 'abc'

# # class Derived(Base):
# #     print(Base.__annotations__)

# # print(Derived.__annotations__)
# # ===============================
# # from __future__ import annotations
# # def foo(a: "str"): 
# #     pass

# # print(foo.__annotations__)
# # ===========================
# # class Foo:
# #     """
# #     name is siyamak
# #     """
# #     def foo(self):
# #         pass
# # n = Foo()
# # print(n.__doc__)
# # =========================

# class N():
#     def __init__(self, age):
#         self.age = age
        
#     def foo(self):
#         return self.age

#     @staticmethod
#     def bar(x, y):
#         print(x + y)

# n = N(5)
# n.bar(55,4)
# ==========================
"""
    __init_subclass__
"""
# class A:

#     @classmethod #optional
#     def __init_subclass__(cls, name):
#         print("A is subclass B")
#         print(name)
    
# class B(A, name = "ali"):
#     pass
# # ==================================
"""
__missing__: only use for dict if key is missed
"""
# class Mydict(dict):
  
#     def __missing__(self, key):
#         return key


# m = Mydict({'name':'siyamak', 'age':32})

# print(m['name'])
# print(m['age'])
# print(m['color'])
# ============================================
"""
__call__  intance of class will be a funcion
"""
# class N:
#     def __call__(self, *args: any, **kwds: any) -> any:
#         print(f"hello call ....{args}-{self}")
# n = N()
# n("siyamak")
# ===============================================
"""
__bool__
"""
# class N:
#     def foo(self):
#         print("")
    
#     def __len__(self):
#         return False

# n = N()
# print(bool(n))
# ----------------------------------------------
# class N:
#     def __init__(self, name):
#         self.name = name

#     def foo(self):
#         print(self.name)
    
#     def __bool__(self):
#         return False

# n = N("saed")
# if n:
#     n.foo()
#     print (True)
# else:
#     print(False)
# ==========================================
"""
__getattr__
"""
class N:
    name = "siyamak"

n = N()
print(n.name)