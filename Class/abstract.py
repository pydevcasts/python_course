"""
Abstract class , Abstract method
"""

from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractmethod
#     def show(self):
#         print("I am a method of Abstract class")

# class B(A):
#     pass

# b = B()
# ====================================
# class A(ABC):
#     @abstractmethod
#     def show(self):
#         print(f"I am a method of Abstract class")

# class B(A):
#     def show(self):
#         super().show()
#         print(f"i am a metod of class {self.__class__}")

# b = B()
# b.show()
# ===============================
# در صورتی که از ابسترکت کلاس استفاده نکنیم
# class A():
#     def show(self):
#         raise NotImplementedError

# class B(A):
#     pass
#     # def show(self):
#     #     print(f"i am a metod of class {self.__class__}")

# b = B()
# b.show()
#########################################
