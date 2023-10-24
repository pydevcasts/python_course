# ایجاد سریع ویژگی‌ها:
#  با استفاده از

#  @dataclass
#  شما نیازی به نوشتن کد مکرر برای ایجاد ویژگی‌ها و متدهای
#  خاص
#  (مانند __init__ و __repr__)
#  ندارید.
#  تمام این کارها به صورت خودکار انجام می‌شوند.
######################################################
# from dataclasses import dataclass
# @dataclass
# class Fruit:
#     name: str
#     cost: float

# banana = Fruit("Banana", 10)
# apple = Fruit("Apple", 5)
# other = Fruit("Banana", 10)
# print(banana)
# print(banana == other)
# print(banana == apple)
# print(type(banana.cost))
# 33
###################################################3
from dataclasses import dataclass
from typing import List

# @dataclass
# class Person:
#     name: str
#     age: int

# @dataclass
# class Address:
#     street: str
#     city: str

# @dataclass
# class Contact(Person, Address):
#     phone_numbers: List[str]

# # Creating an instance of Contact
# contact = Contact(name="John", age=30, street="123 Main St", city="New York", phone_numbers=["123-456-7890"])

# # Accessing properties of the Contact class
# print(contact.name)  # John
# print(contact.street)  # 123 Main St
# print(contact.phone_numbers)  # ['123-456-7890']
###################################################################3
