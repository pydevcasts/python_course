pi = 3.14  # float number
print(type(pi))
# Output class 'float'

# converting float integer
num = int(pi)
print("Integer number:", num)
# Output  3
print(type(num))
# Output class 'int'


# ==================================
flag_true = True
flag_false = False
print(type(flag_true))
# Output class 'bool'

# converting boolean to integer
num1 = int(flag_true)
num2 = int(flag_false)

print("Integer number 1:", num1)  
# Output 1
print(type(num1))  
# Output class 'int'

print("Integer number 2:", num2)
# 0
print(type(num2))
# class 'int'
# ===========================================
string_num = "225"
print(type(string_num))
# Output class 'str'

# converting str to integer
num1 = int(string_num)

print("Integer number 1:", num1)
# Output 225
print(type(num1))
# Output class 'int'
# ======================================
num = 725
print(type(num))
# Output class 'int'

# converting float to integer
num1 = float(num)

print("Float number:", num1)
# Output 725.0
print(type(num1))
# Output class 'float'
# ===============================================

flag_true = True
flag_false = False
print(type(flag_true)) 
# Output class 'bool'

# converting boolean to float
num1 = float(flag_true)
num2 = float(flag_false)

print("Float number 1:", num1)
# Output 1.0
print(type(num1))
# class 'float'

print("Float number 2:", num2)
# Output 0.0
print(type(num2))
# class 'float'
# ======================================================
string_num = "725.535"
print(type(string_num))
# Output class 'str'

# converting str to float
num1 = float(string_num)

print("Float number:", num1)
# Output 725.535
print(type(num1))
# class 'float'

# ==================================================
r_num = 135
print(type(r_num)) # class 'int'

# converting int to complex(x)
c_num = complex(r_num)

print("Complex number:", c_num)
# Output (135+0j)
print(type(c_num))
# class 'complex'

# converting int to complex(x, y)
r_num, i_num2 = 135, 235
c_num = complex(r_num, i_num2)

print("Complex number:", c_num)
# Output (135+235j)
print(type(c_num))  # class 'complex'
# ============================================
r_num = 53.250
print(type(r_num))  # class 'float'

# converting float to complex(x)
c_num = complex(r_num)

print("Complex number:", c_num)
# Output (53.25+0j)
print(type(c_num))  
# class 'complex'

# converting float to complex(x, y)
r_num, i_num2 = 53.250, 350.750
c_num = complex(r_num, i_num2)

print("Complex number:", c_num)
# Output (53.25+350.75j)
print(type(c_num))
# class 'complex'

# ==========================================
boolean_true = True
print(type(boolean_true))  # class 'bool'

# converting boolean to complex(x)
c_num = complex(boolean_true)

print("Complex number:", c_num)  
# Output (1+0j)
print(type(c_num))
# class 'complex'

# converting boolean to complex(x, y)
r_bool, i_bool = False, True
c_num = complex(r_bool, i_bool)

print("Complex number:", c_num)
# Output 1j
print(type(c_num))
# class 'complex'
# =========================================
num1 = 10
num2 = 0
print(type(num1))  # class 'int'

# Convert into to bool
b1 = bool(num1)
b2 = bool(num2)

print(b1)
# Output True
print(b2)
# Output False

print(type(b1))
# class 'bool'
# ======================================
f_num1 = 25.35
f_num2 = 0.0
print(type(f_num1))  # class 'float'

# Convert float into to bool
b1 = bool(f_num1)
b2 = bool(f_num2)

print(b1)
# Output True

print(b2)
# Output False

print(type(b1))
# Output class 'bool'

# ============================================
s1 = "False"
s2 = "True"
s3 = "812"
s4 = ""
print(type(s1))  # class 'str'

# Convert string into to bool
b1 = bool(s1)
b2 = bool(s2)
b3 = bool(s3)
b4 = bool(s4)

print(b1)  # True
print(b2)  # True
print(b3)  # True
print(b4)  # False
print(type(b1))  # class 'bool'

# ==========================================

c1 = 33 + 9j
c2 = 0 + 0j
print(type(c1))  # class 'complex'

# Convert complex value into to bool
b1 = bool(c1)
b2 = bool(c2)

print(b1)  # True
print(b2)  # False
print(type(b1))  # class 'bool'
# ============================================
num = 15
print(type(num))  # class 'int'

# converting int to str type
s1 = str(num)
print(s1)
# Output '15'
print(type(s1))
# Output class 'str'

# ======================================
num = 75.35
print(type(num))  # class 'float'

# converting float to str type
s1 = str(num)
print(s1)
# Output '75.35'
print(type(s1))
# Output class 'str'

# ==========================================
complex_num = 15 + 5j
print(type(complex_num))  # class 'complex'

# converting complex to str type
s1 = str(complex_num)
print(s1)
# Output '(15+5j)'

print(type(s1))
# class 'str'

# ============================================
b1 = True
b2 = False
print(type(b1))  # class 'bool'

# converting bool to str type
s1 = str(b1)
s2 = str(b2)
print(s1)
# Output 'True'
print(s2)
# Output 'False'
print(type(s1))  # class 'str'

# =================================================
