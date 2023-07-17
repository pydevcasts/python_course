# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# ================================================================
# The try block will generate an exception, because x is not defined:

# try:
#   print(x)
# except:
#   print("An exception occurred")
# ==========================================================
#This will raise an exception, because x is not defined:
# print(x)
# =============================================
# Print one message if the try block raises a NameError and another for other errors:

# try:
#   print(x)
#   y = int(input("what is your number? \n"))
#   print(y)
# except ValueError:
#   print("Variable x is not defined")
# except NameError:
#   print("Something else went wrong")
# except :
#     print("sfgvsd")
# =====================================
# In this example, the try block does not generate any error:
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
# =========================================
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
# =============================================
# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
# =======================================
# Raise an error and stop the program if x is lower than 0:
# x = -1

# if x < 0:
#   raise Exception
# ===================================
# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")
# ====================================
# s = 'apple'
# try:
# 	num = int(s)
# except ValueError:
# 	raise ValueError("String can't be changed into integer")

