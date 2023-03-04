# variable_name = variable_value

name = "John"  # string assignment
age = 25  # integer assignment
salary = 25800.60  # float assignment

print(name)  # John
print(age)  # 25
print(salary)  # 

# =====================================
var = 10
print(var)  # 10
# print its type
print(type(var))  # <class 'int'>

# assign different integer value to var
var = 55
print(var)  # 55

# change var to string
var = "Now I'm a string"
print(var)  # Now I'm a string
# print its type
print(type(var))  # <class 'str'>

# change var to float
var = 35.69
print(var)  # 35.69
# print its type
print(type(var))  # <class 'float'>

# create integer variable
age = 28
print(age)  # 28
print(type(age))  # <class 'int'>

a = 3 + 5j
print(a)  # (3+5j)
print(type(a))  # <class 'complex'>
# =========================================


# create a variable of type string
str = 'PYnative'
# prints complete string
print(str)  # PYnative

# prints first character of the string
print(str[0])  # P

# prints characters starting from 2nd to 5th
print(str[2:5])  # nat

# length of string
print(len(str))  # 8

# concatenate string
print(str + "TEST")  # PYnativeTEST

# ==========================================

# create list
my_list = ['Jessa', 10, 20, 'Kelly', 50, 10.5]
# print entire list
print(my_list)  # ['Jessa', 10, 20, 'Kelly', 50, 10.5]

# Accessing 1st element of a list
print(my_list[0])  # 'Jessa'

# Accessing  last element of a
print(my_list[-1])  # 10.5

# access chunks of list data
print(my_list[1:3])  # [10, 20]

# Modifying first element of a list
my_list[0] = 'Emma'
print(my_list[0])  # 'Emma'

# add one more elements to list
my_list.append(100)
print(my_list)  # ['Emma', 10, 20, 'Kelly', 50, 10.5, 100]

# ===============================================

a = 100
print(type(a))  # class 'int'

b = 100.568
print(type(b))  # class 'float'

str1 = "PYnative"
print(type(str1))  # class 'str'

my_list = [10, 20, 20.5, 100]
print(type(my_list))  # class 'list'

my_set = {'Emma', 'Jessa', 'Kelly'}
print(type(my_set))  # class 'set'

my_tuple = (5, 10, 15, 20, 25)
print(type(my_tuple))  # class 'tuple'

my_dict = {1: 'William', 2: 'John'}
print(type(my_dict))  # class 'dict'

# ========================================

my_list =[10,20,20.5,'Python',100]
# It will print only datatype of variable
print(type(my_list).__name__) # list

# ==========================================
var1 = 100
del var1
print(var1)

# ================================

a = 100
A = 200

# value of a
print(a)  # 100
# Value of A
print(A)  # 200

a = a + A
print(a)  # 300
# ==============================

# ca$h = 1000

# ca$h = 11
    #   ^
# SyntaxError: invalid syntax
# ==================================

total = 120
Total = 130
TOTAL = 150
print(total)
print(Total)
print(TOTAL)

# ===============================
# Multiple assignments
a = b = c = 10
print(a) # 10
print(b) # 10
print(c) # 10

# =================================

def test1():  # defining 1st function
    price = 900  # local variable
    print("Value of price in test1 function :", price)

def test2():  # defining 2nd function
    # NameError: name 'price' is not defined
    print("Value price in test2 function:", price)

# call functions
test1()
test2()
# ======================================


price = 900  # Global variable

def test1():  # defining 1st function
    print("price in 1st function :", price)  # 900

def test2():  # defining 2nd function
    print("price in 2nd function :", price)  # 900

# call functions
test1()
test2()
# ========================================


n = 300
m = n
print(id(n)) # same memory address
print(id(m)) # same memory address 

# =======================================
a = 10
b = 10
print(id(a))
print(id(b))

c = 20
d = 20
e = 20
print(id(c))
print(id(d))
print(id(e))

# 140722211837248
# 140722211837248
# 140722211837568
# 140722211837568
# 140722211837568
# ===================================

# paking a collection into a variable

a = 10
b = 20
c = 20
d = 40
tuple1 = a, b, c, d # Packing tuple
print(t) # (10, 20, 20, 40)
# ====================================
# unpacking

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a, b, c, d)  # 10 20 30 40

# ====================================
# Instance Variables and class variable


class Student:
    # Class variable
    school_name = 'ABC School '
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create first object
s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

# create second object
s2 = Student('Jessa', 20)
# access instance variable
print(s2.name, s2.roll_no)
# access class variable
print(Student.school_name)

# ======================================================

















