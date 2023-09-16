# 


from sys import argv

# print(type(argv))
# Output <class 'list'>
# ============================================

# for i in argv:
#     print(i)


# ==================================

# calculate the addition of two command line input

# add = int(argv[1]) + int(argv[2])
# print('Addition is:', add)
# python index.py 20 30
# print(argv[2])
# Addition is: 50
# =========================================

# print(argv[2])
# print(argv[3])
# python index.py 20
# Traceback (most recent call last):
#   File "sample.py", line 3, in <module>
#     print(argv[2])
# IndexError: list index out of range


# =========================================
import sys

# print(dir(sys))
sys.path.append("/mymodule")
# print(sys.path)
# print(sys.maxsize)
# print(sys.executable)
# print(sys.platform)
# print(sys.version)
# sys.stdout.write('python') #A built-in file object that is analogous to the interpreter’s standard output stream in Python.
                            #stdout is used to display output directly to the screen

# import time

# if sys.platform == "linux":
#     sys.exit()
# else:
#     time.sleep(5)

# print(sys.argv[1])


# if sys.argv[1] == "admin":
#     print("login complete")
# else:
#     print("user or password is wrong")


