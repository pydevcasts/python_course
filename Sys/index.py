# 


from sys import argv

print(type(argv))
# Output <class 'list'>
# ============================================

import sys
for i in sys.argv:
    print(i)


# ==================================
from sys import argv

# calculate the addition of two command line input
print('Argument one:')
print('Argument Two:')
add = int(argv[1]) + int(argv[2])
print('Addition is:', add)
# python index.py 20 30
# Argument one:
# Argument Two:
# Addition is: 50
# =========================================

from sys import argv

print(argv[2])
print(argv[3])
# python index.py 20
# Traceback (most recent call last):
#   File "sample.py", line 3, in <module>
#     print(argv[2])
# IndexError: list index out of range