# store int value
roll_no = 33
# display roll no
print("Roll number is:", roll_no)
# output 33
print(type(roll_no))  
# output class 'int'

# store integer using int() class
id = int(25)
print(id)  # 25
print(type(id))  # class 'int'
# =======================================

# decimal int 16 with base 8
# Prefix with zero + letter o
octal_num = 0o20
print(octal_num)  # 16
print(type(octal_num))  # class 'int'

# decimal int 16 with base 16
# Prefix with zero + letter x
hexadecimal_num = 0x10  # decimal equivalent of 21
print(hexadecimal_num)  # 16
print(type(hexadecimal_num))  # class 'int'

# decimal int 16 with base 2
# Prefix with zero + letter b
binary_num = 0b10000  # decimal equivalent of 6
print(binary_num)  # 16
print(type(binary_num))  # class 'int'

# =============================================


# store a floating-point value
salary = 8000.456
print("Salary is :", salary)  # 8000.456
print(type(salary))  # class 'float'

# store a floating-point value using float() class
num = float(54.75)
print(num)  # 54.75
print(type(num))  # class 'float'

# ========================================

# exponential float
num1 = 1.22e4
print(num1)  # 12200.0
print(type(num1))  # class 'float'

# =========================================

x = 9 + 8j  # both value are int type
y = 10 + 4.5j  # one int and one float
z = 11.2 + 1.2j  # both value are float type
print(type(x))  # class 'complex'>

print(x)  # (9+8j)
print(y)  # (10+4.5j)
print(z)  # (11.2+1.2j)

# =====================================


my_list = ["Jessa", "Kelly", 20, 35.75]
# display list
print(my_list)  # ['Jessa', 'Kelly', 20, 35.75]
print(type(my_list))  # class 'list'

# Accessing first element of list
print(my_list[0])  # 'Jessa'

# slicing list elements
print(my_list[1:5])  # ['Kelly', 20, 35.75]

# modify 2nd element of a list
my_list[1] = "Emma"
print(my_list[1])  # 'Emma'

# create list using a list class
my_list2 = list(["Jessa", "Kelly", 20, 35.75])
print(my_list2)  # ['Jessa', 'Kelly', 20, 35.75]

# =============================================

# create a tuple
my_tuple = (11, 24, 56, 88, 78)
print(my_tuple)  # (11, 24, 56, 88, 78)
print(type(my_tuple))  # class 'tuple'

# Accessing 3rd element of a tuple
print(my_tuple[2])  # 56

# slice a tuple
print(my_tuple[2:7])  # (56, 88, 78)

# create a tuple using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)  # (10, 20, 30, 40)
# =========================================

# create a tuple
my_tuple = (11, 24, 56, 88, 78)

# modify 2nd element of tuple
my_tuple[1] = 35
print(my_tuple)
# TypeError: 'tuple' object does not support item assignment

# =======================================

# create a dictionary
my_dict = {1: "Smith", 2: "Emma", 3: "Jessa"}

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# create a dictionary using a dit class
my_dict = dict({1: "Smith", 2: "Emma", 3: "Jessa"})

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# access value using a key name
print(my_dict[1])  # Smith

# change the value of a key
my_dict[1] = "Kelly"
print(my_dict[1])  # Kelly

# ===================================

# create a set using curly brackets{,}
my_set = {100, 25.75, "Jessa"}
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# create a set using set class
my_set = set({100, 25.75, "Jessa"})
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# add element to set
my_set.add(300)
print(my_set)  # {25.75, 100, 'Jessa', 300}

# remove element from set
my_set.remove(100)
print(my_set)  # {25.75, 'Jessa', 300}

# ===========================================

my_set = {11, 44, 75, 89, 56}
print(type(my_set))  # class 'set'

# creating frozenset
f_set = frozenset(my_set)
print(type(f_set))  # class 'frozenset'
# ======================================

x = 25
y = 20

z = x > y
print(z)  # True
print(type(z))  # class 'bool'
# ===================================

a = [9, 14, 17, 11, 78]
b = bytes(a)
print(type(b))  # class 'bytes'
print(b[0])  # 9
print(b[-1])  # 78

# ============================================
a = [999, 314, 17, 11, 78]  # Gives error range must be in 0 to 256
b = bytes(a)
print(type(b))
# ValueError: bytes must be in range(0, 256)

# ============================================

# create a bytearray
list1 = [9, 17, 11, 78]
b_array = bytearray(list1)
print(b_array)
print(type(b_array))  # class 'bytearray'

# modifying bytearray
b_array[1] = 99
print(b_array[1])  # 99

# iterate bytearray
for i in b_array:
    print(i, end=" ")  # 9 99 11 78

# =====================================

# Generate integer numbers from 10 to 14
numbers = range(10, 15, 1)
print(type(numbers))  # class 'range'

# iterate range using for loop
for i in range(10, 15, 1):
    print(i, end=" ")
# Output 10 11 12 13 14

# =======================================

# Generate integer numbers from 10 to 14
numbers = range(10, 15, 1)
print(type(numbers))  # class 'range'

# iterate range using for loop
for i in range(10, 15, 1):
    print(i, end=" ")
# Output 10 11 12 13 14

# =========================================

byte_array = b'PYnative'      # creating bytes array object
byte_array_view = memoryview(byte_array)  # creating memory view for bytes array objects
container = tuple(byte_array_view)   # Storing it in container of iterating
for char in container:
    print(char, end=" ")
# output
# 80 89 110 97 116 105 118 101
# ====================================
