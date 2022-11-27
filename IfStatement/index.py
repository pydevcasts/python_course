number = 6
if number > 5:
    # Calculate square
    print(number * number)
print('Next lines of code')
# ====================================
password = input('Enter password ')

if password == "123456789":
    print("Correct password")
else:
    print("Incorrect Password")

# ==============================================
def user_check(choice):
    if choice == 1:
        print("Admin")
    elif choice == 2:
        print("Editor")
    elif choice == 3:
        print("Guest")
    else:
        print("Wrong entry")

user_check(1)
user_check(2)
user_check(3)
user_check(4)
# ==================================================
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is greater than', num2)
else:
    print(num1, 'is smaller than', num2)

# ===============================================
for i in range(1, 11):
    print(i)
# =================================================
num = 10
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("Sum of first 10 number is:", sum)
# =================================================
for num in range(10):
    if num > 5:
        print("stop processing.")
        break
    print(num)
# ==========================================

for num in range(3, 8):
    if num == 5:
        continue
    else:
        print(num)
# ======================================
months = ['January', 'June', 'March', 'April']
for mon in months:
    pass
print(months)
# ['January', 'June', 'March', 'April']
# ==========================================
