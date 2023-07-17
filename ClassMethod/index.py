import datetime

# =======================================
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
# =========================================
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# ========================================
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1
try:
    print(p1)
except:
    raise NameError("p1 is removed by siyamak")
# ========================================
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