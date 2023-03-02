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

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"{self.name} is {self.age} years old")

    @classmethod
    def birth(cls, name, age):
        return cls(name, datetime.datetime.now().year - age)

    @staticmethod
    def is_adult(age):
        if age > 35:
            print("young adoult")
        else:
            print("he is teen")

p = Person.is_adult(42)