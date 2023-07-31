"""
__new__

وظیفه‌ی متد __new__ این هست که
instance
رو برگردونه
اگر این متد چیزی رو برنگردونه متد
__init__
هم اجرا نمیشه.

وقتی می‌گیم که 
__init__ 
تابع سازنده نیست 
به این خاطر هست که
 شما داخل __init__
  به آبجکت دسترسی دارید
  
"""


class A:
    def __init__(self, name):
        print(self)
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        print(cls)
        if name == "siyamak":
            return None
        else:
            return super().__new__(cls, *args, **kwargs)

    def show(self):
        print(self.name)


a = A("siyamak")
print(a)
a.show()
