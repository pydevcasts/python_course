class Person():
    def __init__(self, name) -> None:
        self.name = name

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
class Car():
    def __init__(self, color) -> None:
        self.__color = color

class Profile(Car):
    def __init__(self, name, color) -> None:
        super().__init__(color)
        self.name = name

profile = Profile("siyamak", "red")
print(dir(profile))
print(profile._Car__color)
print(profile.name)
