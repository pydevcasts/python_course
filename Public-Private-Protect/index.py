class Person():
    def __init__(self, name) -> None:
        self._name = name

person = Person("siyamak")
# print(person)
# print(person.name)
# print(dir(person))
    

# ===============================
# class Profile():
#     def __init__(self, age) -> None:
#         self._age = age

# profile = Profile(35)
# print(dir(profile))
# print(profile._age)
# ====================================
# class Profile(Person):
#     def __init__(self, name,age) -> None:
#         super().__init__(name)
#         self._age = age

# profile = Profile("siyamak", 43)
# print(dir(profile))
# print(profile._age)
# print(profile.name)
# ======================================
# class Car():
#     def __init__(self, color) -> None:
#         self.__color = color

# class Profile(Car):
#     def __init__(self, name, color) -> None:
#         super().__init__(color)
#         self.name = name

# profile = Profile("siyamak", "red")
# print(dir(profile))
# print(profile._Car__color)
# print(profile.name)
# ==============================================
# Creating a class
# class A:

# 	# Declaring public method
# 	def fun(self):
# 		print("Public method")

# 	# Declaring private method
# 	def __fun(self):
# 		print("Private method")


# # Driver's code
# obj = A()
# print(dir(obj))
# # Calling the private member
# # through name mangling
# obj._A__fun()
# ==========================================
# Creating a class
# class A:

# 	# Declaring public method
# 	def fun(self):
# 		print("Public method")

# 	# Declaring private method
# 	def __fun(self):
# 		print("Private method")

# 	# Calling private method via
# 	# another method
# 	def Help(self):
# 		self.fun()
# 		self.__fun()


# # Driver's code
# obj = A()
# obj.Help()
# =============================================
class Base:
	def fun(self):
		print("Public method")

	def __fun(self):
		print("Private method")

class Derived(Base):
	def __init__(self):
		Base.__init__(self)

	def call_public(self):
		print("\nInside derived class")
		self.fun()

	def call_private(self):
		self.__fun()

obj1 = Base()
obj1.fun()
obj1._Base__fun()
obj2 = Derived()
print(dir(obj2))
# obj2.call_private()

# Uncommenting obj1.__fun() will
# raise an AttributeError

# Uncommenting obj2.call_private()
# will also raise an AttributeError
# ==========================================
# # class N:
# #     _age = 42
# #     __name = "mohammad"
# #     def foo(self):
# #         return self._age, self.__name
# # n = N()
# # print(n.foo())
# # print(N._age)
# # print(N.__name__)