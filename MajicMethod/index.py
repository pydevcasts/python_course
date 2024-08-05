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


# class N:
#     def __init__(self, value):
#         self.value = str(value)

#     def __str__(self):
#         return (self.value) + "5"

#     def __float__(self):
#         return type(float(self.value))

# n = N(5)
# print(n.__str__())
# print(n.__float__())
# # ===============================
# # def foo(arg:int)->str:
# #     print(foo.__annotations__)
# #     print(foo.__annotations__.get('arg'))
# #     print(type(arg))
# # foo(10)
# foo("12")

# # {'arg': <class 'int'>, 'return': <class 'str'>}
# # <class 'int'>
# # <class 'int'>
# # {'arg': <class 'int'>, 'return': <class 'str'>}
# # <class 'int'>
# # <class 'str'>
# # =================================

# # class Foo:
# #     """
# #     name is siyamak
# #     """
# #     def foo(self):
# #         pass
# # n = Foo()
# # print(n.__doc__)
# # =========================

"""
__\ng__: only use for dict if key is missed
"""
# class Mydict(dict):
  
#     def __missing__(self, key):
#         return key, "key is not exists"


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
# class N:
#     name = "siyamak"
#     age = 41

#     def __getattr__(self, item):
#         return f"{item} doesnot exists"
#     """This is priority whole of your code"""


#     def __getattribute__(self,item):
#         if item == "age":
#             return super().__getattribute__(item) + 1

#         elif item == "name":
#                 return f"the name of attr is :{super().__getattribute__(item)}"
#         else:
#             return "doest not exists"

        

# n = N()
# print(n.age)
# print(n.names)
# =============================================
"""
__setattr__
"""
# class N:
#     name = "sia"
#     def __setattr__(self,key, value):
#         if key == "age":
#             raise KeyError("you can change that")
#         return super().__setattr__(key, value)
# n = N()
# n.name = "ali"
# print(n.name)
# ================================================
"""
__delattr__
"""
# class N:
#     age = 42
#     def __delattr__(self,key):
#         if key == "age":
#             print("You cannot delete key")
#         else:
#             return super().__delattr__(key)
# n = N()
# n.name = "siyamak"
# del n.name 
# print(n.name)

# ==========================================
""" __add__"""
# class Machine:
# 	""" Class doc string  """
# 	def __init__(self,brand):
# 		self.brand = brand
		
# 	def __add__(self, other):
# 		return Machine(self.brand + other.brand)

# #create an instance
# mustang = Machine(5)
# mustang1 = Machine(50)
# p=mustang+mustang1
# print(p.brand)
# =========================================
"""__iadd__"""
# class N:
#     def __init__(self,a,b, *args):
#         self.a = a
#         self.b = b
    
#     def __iadd__(self, other):
#         return self.a + other.a , self.b + other.b
    
# n = N(2,3)
# m = N(2,3)
# n += m """this is diff bettween __add__ and __iadd__"""
# print(n + m)
#################################################
"""__reversed__"""
# arr = [1,2,3,4,5]
# print(list(reversed(arr)))

# class N:
#     def __init__(self, num):
#         self.num = num
#     def __reversed__(self):
#         return list(reversed(self.num))
# n = N([1,2,3,45])
# print(reversed(n))
# ======================================
"""__gt__"""
# class Distance:
#   def __init__(self, x=None,y=None):
#       self.x=x
#       self.y=y

#   def __ge__(self, other):
#       val1=self.x*12+self.y
#       val2=other.x*12+other.y
#       if val1>=val2:
#           return True
#       else:
#           return False
          
          
# d1=Distance(20,100)
# d2=Distance(4,10)
# print(d1>=d2)
# # =========================================
# """__gt__"""
# class N:
#     def __init__(self, x = None, y = None):
#         self.x = x
#         self.y = y

#     def __gt__(self, other):
#         val1 = self.x*12+self.y
#         val2 = other.x*12+other.y
#         if val1>val2:
#             return True
#         else:
#             return False

# n = N(20, 100) #this is x, y
# m = N(4,100)   #this is other a and ather y
# print(n>m)
##############################################
# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __contains__(self, item):
#         return item in self.value
# n = Number([1,2,3,4,5])
# print(4 in n)
#############################################

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __iter__(self):
#         for item in range(self.value):
#             yield item * 2

# n = iter(Number(5))
# print(next(n))
# print(next(n))
###################################################
class Inventory:
    
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)


    def __len__(self):
        return len(self.slots)

    
    def __contains__(self, item):
        return item in self.slots
    
    def __iter__(self):
        yield from self.slots


    def __getitem__():
        pass
############################################################
class N:
    def __init__(self, value):
        if isinstance(value, list):
            self.value = tuple(value)
        else:
            self.value = value
    
    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other: object):
        if isinstance(other, N):
            return self.value == other.value
        return False

n = N([1,2])
m = N([3,4])
print(hash(n))
print(n is m)
