# keyword.kwlist: It return a sequence containing all the keywords defined for the interpreter.
# keyword.issoftkeyword(s): Return True if s is a Python soft keyword. New in version 3.9
# keyword.softkwlist: Sequence containing all the soft keywords defined for the interpreter. New in version 3.9





import keyword
print(keyword.kwlist)
print(keyword.iskeyword('if'))
print(keyword.iskeyword('range'))



# Understand Any keyword
# The python help() function is used to display the documentation of modules, functions, classes, keywords.

print(help('if'))

# =============================================

x = 10
y = 20

# and to combine to conditions
# both need to be true to execute if block
if x > 5 and y < 25:
    print(x + 5)

# or condition
# at least 1 need to be true to execute if block
if x > 5 or y < 100:
    print(x + 5)

# not condition
# condition must be false
if not x:
    print(x + 5)

    # output =15 15

# ====================================================


my_list = [11, 15, 21, 29, 50, 70]
number = 15
if number in my_list:
    print("number is present")
else:
    print("number is not present")


# ==========================================================


x = 75
if x > 100:
    print('x is greater than 100')
elif x > 50:
    print('x is greater than 50 but less than 100')
else:
    print('x is less than 50')

# =================================================


print('for loop to display first 5 numbers')
for i in range(5):
    print(i, end=' ')

print('while loop to display first 5 numbers')
n = 0
while n < 5:
    print(n, end=' ')
    n = n + 1

# =========================================


# def keyword: create function
def addition(num1, num2):
    print('Sum is', num1 + num2)

# call function
addition(10, 20)


# =======================================

# pass keyword: create syntactically empty function
# code to add in future
def sub(num1, num2):
    pass
# ================================================

# create class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# create object
s = Student('Jessa', 19)
# call method
s.show()
# ===============================================

# Opening file
with open('sample.txt', 'r', encoding='utf-8') as fp:
    # read sample.txt
    print(fp.read())

# ==========================================

import datetime

# get current datetime
now = datetime.datetime.now()
print(now)

# ========================================

