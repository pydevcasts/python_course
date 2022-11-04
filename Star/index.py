num = int(input("enter you number?\n"))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end = " ")
    print()
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# ------------------------------------------------

for row in range(7):
    for col in range(5):
        if ((col == 0 or col == 4 ) and row != 0) or\
             ((row == 0 or row == 3) and (col > 0 and col < 4)):
            print("*", end = "")
        else:
            print(end = " ")
    print()

#  *** 
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

# ---------------------------------------------------


for row in range(5):
    for col in range(4):
        if ((row == 4 or row == 0 or row == 2) or (col==0 or col == 3)):
            print("*", end = "")
        else:
            print(end =" ")
    print()

# ****
# *  *
# ****
# *  *
# ****

for row in range(5):
    for col in range(4):
        if ((col == 0 or col == 3) and (row == 0 or row == 4)):
            print("*", end = "")
        else:
            print(end = " ")
    print()

# *  *
    
# *  *

# ------------------------------------------------------
for row in range(5):
    for col in range(5):
        if((row == 0 or row == 2 or row == 4 ) and col != 4) \
           or (col == 0) or (col == 4 and (row !=0 and row != 2 and row != 4))  :
            print("*", end = "")
        else:
            print(end = " ")
    print()

# **** 
# *   *
# **** 
# *   *
# **** 
# ---------------------------------------------------------

for row in range(4):
    for col in range(6):
        if ((row == 3) or (row == 2 and (col != 0 and col != 5)) or (row == 1 and (col != 0 and col != 1 and col != 5 and col != 4))):
            print("*", end = "")
        else:
            print(end = " ")
    print()

#   **  
#  **** 
# ******
# ------------------------------------------------------
# or mean we have and mean dont have

