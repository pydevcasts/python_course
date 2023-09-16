# بد
def calculate_square_and_cube(number):
result_square=number **2
result_cube=number**3
return result_square,result_cube
# خوب 
def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# ===========================================
# بد
class MyPerson:
def __init__(self,name,age):
self.name=name
self.age=age
def displayInfo(self):
print("Name:",self.name,"Age:",self.age)

# خوب
class MyPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print("Name:", self.name, "Age:", self.age)
# ===============================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print("Name:", self.name, "Age:", self.age)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def display_info(self):
        print("Make:", self.make, "Model:", self.model)



def calculate_square(number):
    square = number ** 2
    return square


def calculate_cube(number):
    cube = number ** 3
    return cube
# =============================================
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def display_info(self):
        print("Make:", self.make, "Model:", self.model)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print("Name:", self.name, "Age:", self.age)


def calculate_square(number):
    square = number ** 2
    return square


def calculate_cube(number):
    cube = number ** 3
    return cube


def main():
    car = Car("Toyota", "Camry")
    car.display_info()
    
    person = Person("John", 30)
    person.display_info()
    
    num = 5
    squared = calculate_square(num)
    cubed = calculate_cube(num)
    print("Number:", num, "Squared:", squared, "Cubed:", cubed)


if __name__ == "__main__":
    main()
# ==================================================
print("Hello\!")           # چاپ "Hello!"
print("First\, Second")    # چاپ "First, Second"
# ======================================================
million = 1_000_000  # استفاده از اسناد (_) برای خوانایی در اعداد بزرگ
# ================================================
numbers = 1,000,000, 2,000,000, 3,000,000  # جدا کردن اعداد با کاما
# ================================================
first_name = "John"     # نام‌گذاری با فاصله
last_name = "Doe"

full_name = "John_Doe"  # نام‌گذاری با پایین‌خط
# ===============================================
my_long_list = [
    item1, 
    item2, 
    item3
]
# or 
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
# =================================================
# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
# =============================================

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
# ======================================================

income = (gross_wages 

          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# ==================================================================
# درست:
import os
import sys
# غلط:
import sys, os
# درست
from subprocess import Popen, PIPE




"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys


# =====================================
# درست:
spam(ham[1], {eggs: 2})
# غلط:
spam( ham[ 1 ], { eggs: 2 } )
# ==========================================

# درست:
foo = (0,)
# غلط:
bar = (0, )
# ===========================================
# درست:
if x == 4: print(x, y); x, y = y, x
# غلط:
if x == 4 : print(x , y) ; x , y = y , x
# ==============================================
# درست:
spam(1)
# غلط:
spam (1)
# =========================================
# درست:
dct['key'] = lst[index]
# غلط:
dct ['key'] = lst [index]
# ========================================
# بیش از یک فاصله اطراف عملگر تخصیص = برای تراز کردن کلمات با دیگر خطوط:

# درست:
x = 1
y = 2
long_variable = 3
# غلط:
x             = 1
y             = 2
long_variable = 3
# ==============================================

# درست:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# غلط:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
# ============================================

# انوتیشن‌های توابع باید از قوانین عادی برای دونقطه استفاده کنند و در صورت وجود نشانه پیکان -> همیشه فضای خالی اطراف آن باشد. (برای اطلاعات بیشتر به انوتیشن‌های توابع مراجعه کنید.):

# درست:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...

# غلط:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
# ====================================================

# به هنگام نشان دادن یک آرگومان، یا نشان دادن مقدار پیش‌فرض پارامتر یک تابع unannotated از فضای خالی اطراف علامت = استفاده نکنید:

# درست:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
# غلط:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
# ===========================================================
با این حال، هنگام تخصیص مقدار پیش‌فرض به یک انوتیشن، از فضای خالی اطراف علامت = استفاده کنید:

# درست:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
# غلط:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
# ====================================================

# نباید از چندین عبارت دستوری در یک خط استفاده کرد:

# درست:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# نامناسب:

# غلط:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
# =========================================================

# درست:
FILES = ('setup.cfg',)
# غلط:
FIES L= 'setup.cfg',
# ========================================
# درست:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
# غلط:
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)
# =================================================

"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
# برای مستندات یک خطی، لطفاً """ پایانی را در همان خط قرار دهید:

"""Return an ex-parrot."""
# ======================================

# درست:
if foo is not None:
# غلط:
if not foo is None:
# ===================================
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
# غلط:
try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)
# =======================================
 
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
# غلط:

def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)
# ==============================================
# متدهای startswith() و endswith() تمیزتر و کم‌خطاتر هستند:

# درست:
if foo.startswith('bar'):
# غلط:
if foo[:3] == 'bar':
# ===============================================
# در هنگام مقایسه‌ی اشیاء بجای مقایسهٔ نوع آن‌ها به صورت مستقیم، همیشه از متد isinstance() استفاده کنید:

# درست:
if isinstance(obj, int):
# غلط:
if type(obj) is type(1):
# =====================================
if not seq:
if seq:
# غلط:
if len(seq):
if not len(seq):
# =========================================
# مقادیر بولی را با استفاده از == با True و False مقایسه نکنید:

# درست:
if greeting:
# غلط:
if greeting == True:

# بدترین:
# غلط:
if greeting is True:
# ===================================