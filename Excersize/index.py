
# x = "hasan"
# for i in range(0, 4):
#     print(x)


# =========================

# number = [8,1,7,2,3,6,4,9]
# for i in range(0, 8, 2):
#     print(number[i])

# ==========================


# basket = ["orange", "kiwi", "cherry"]
# user = input("what did you buy?\n")

  
# if user in basket:
#     print("before you bougth")
# else:
#     basket.append(user)
# print(basket)
# ===========================================


# number = list(input("Enter your number?\n"))
# list_number = number
# print(list_number)
# for i in range(0,len(list_number), 2):
#     print(list_number[i])

# =============================


# number = [8,1,7,2,3,6,4,9]

# number.sort()
# print(number)
# for i in range(0, len(number), 2):
#     print(number[i])

# ==========================

# number = [8,1,7,2,3,6,4,9]
# number.sort()

# for i in range(len(number)):
#     if number[i] % 2 == 0:
#         print(number[i])

# ==========================

# x = [1,8,10,9,4,6]
# y = 0
# for i in range(len(x)):
#     while x[y] < x[i]:
#         x[y] = x[y + 1]
#         y +=1
# print(x[y])
# ===========================
# Max .
# x = ["ali", "siyamak", "mahdi"]
# y = 0
# for i in range(len(x)):
#     while x[y] < x[i]:
#         x[y] = x[y + 1]
#         y +=1
# print(x[y])

# ==================================
# Max with for 
# x = [1,2,9,5,8,4,11,33,22,55,999,77]
# x = ["ali", "siyamak", "mahdi"]
# y = 0
# for i in range(len(x)):
#     if x[y] < x[i]:
#         x[y] = x[y + 1]
  
# print(x[y])
# ====================================

# name = {"ali", "hasan", "mahdi", "zahra"}
# y = input("what is your name?\n")
# if y not in name:
#     print("nazanin was not in set")
#     name.update([y])
#     print(name)
# else:
#     print(name)

# ================================



# تمرین برا جلسه یعد

# x = "CatBatSatFatOr"
# out =["Cat", "Bat", "Sat", "Fat", "Or"]  خروجی این باشد
# x = "CatBatSatFatOr"
# demo = []
# for i in range(0, len(x), 3):
#     demo.append(x[i:i+3])
# print(demo)
# # =========================


# ایتم تکراری رو توی این لیست پیدا کن

# x = [1,277,1,4,1,5,3,4,3,2,1]

# # ==========================


# بزرگترین عدد تو لیست نشون بده
# x = [[1, 4, 16, 64],[2,3,4, 1],[3, 6, 9, 12]]
# out = 64 , 4 12 خروجی این ۳ عدد باشد



# fruit = ["kiwi", "bnana", "orange"]

# user_eat = input("what do you want to eat?")
# fruit.remove(user_eat)

# print(fruit)
# ================================
# x = input("what is your name?")
# print(f"salam {type(x)} chetory aya input yad gerefti ya bishtar tozih bedam!")\
# =================================

# x = 0
# i = input("?")
# while x < int(i):
#   x += 1
#   if x % 2 == 0:
#     print(x)




# lst1 = [1, 2, 3]
# lst2 = lst1
# lst3 = lst1.copy()
# lst2[0] = 4
# lst3[1] = 5
# print(lst1,lst2,lst3)


#output
# الف) lst1 = [4, 2, 3], lst2 = [4, 2, 3], lst3 = [1, 5, 3]
# ب) lst1 = [1, 2, 3], lst2 = [4, 2, 3], lst3 = [1, 5, 3]
# ج) lst1 = [4, 2, 3], lst2 = [1, 2, 3], lst3 = [4, 5, 3]
# د) lst1 = [4, 2, 3], lst2 = [1, 2, 3], lst3 = [1, 2, 3]

# ==================================
# lst = [10, 20, 30, 40, 50]
# a = lst[1:4]
# b = lst[:3]
# c = lst[2:]
# d = lst[1:5:2]

# print(a, b,c,d)
# ===============================
# s = {1,2,3}
# s.update({5})
# print(s)
# # print(dir(set))

#############################################
# محاسبه مجموع اعداد یک لیست

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for number in numbers:
#     total += number
# print(total)
#############################################

# چاپ اعضای یک لیست با استفاده از حلقه

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)

#########################################

# جستجوی عنصر در یک لیست

# names = ["Alice", "Bob", "Charlie"]
# search_name = "Bob"
# if search_name in names:
#     print(f"{search_name} found!")
# else:
#     print(f"{search_name} not found!")
##########################################
# اضافه کردن و حذف عناصر از یک لیست

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)  # اضافه کردن عدد 6 به انتهای لیست
# numbers.remove(3)  # حذف عدد 3 از لیست
# print(numbers)
##############################################
# مرتب سازی یک لیست به صورت صعودی یا نزولی

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# numbers.sort()  # مرتب‌سازی به صورت صعودی
# print(numbers)
# numbers.sort(reverse=True)  # مرتب‌سازی به صورت نزولی
# print(numbers)
###########################################
# تبدیل یک لیست به رشته

# characters = ['a', 'b', 'c', 'd']
# result = ''.join(characters)
# print(result)
########################################
# تعویض کاراکترها در یک رشته

# text = "Hello, World!"
# new_text = text.replace('o', '*')
# print(new_text)
##########################################
# جدا کردن یک رشته بر اساس یک کاراکتر خاص

# sentence = "apple,banana,orange"
# fruits = sentence.split(',')
# print(fruits)
# تبدیل یک رشته به لیست کاراکترها
####################################

# word = "Hello"
# characters = list(word)
# print(characters)
#######################################
# تبدیل یک لیست به رشته
# words = ["Hello", "world", "Python"]
# sentence = ' '.join(words)
# print(sentence)
########################################

# جدا کردن یک رشته بر اساس یک کاراکتر خاص

# data = "apple,banana,orange"
# fruits = data.split(',')
# print(fruits)
##################################
# تبدیل یک رشته به لیست کاراکترها

# word = "Python"
# characters = list(word)
# print(characters)
####################################

# جستجوی عنصر در یک لیست

# colors = ["red", "green", "blue", "yellow"]
# search_color = "green"
# if search_color in colors:
#     print(f"{search_color} found!")
# else:
#     print(f"{search_color} not found!")
#######################################
# مرتب سازی یک لیست به صورت صعودی یا نزولی

# numbers = [5, 2, 8, 1, 9]
# numbers.sort()  # مرتب‌سازی به صورت صعودی
# print(numbers)
# numbers.sort(reverse=True)  # مرتب‌سازی به صورت نزولی
# print(numbers)
############################################

# text = "Hello, World!"
# new_text = text.replace('l', 'L')
# print(new_text)
################################
# numbers = [11, 20, 33, 42, 55, 68, 73, 84, 97]

# # Initialize sum
# total = 0

# # Iterate through the list
# for number in numbers:
#     # Check if the number is even
#     if number % 2 == 0:
#         # Add the even number to the total sum
#         total += number

# # Print the total sum of even numbers
# print("The sum of even numbers is:", total)
#####################################################

# محاسبه فاکتوریل یک عدد

# number = 5
# result = 1
# for i in range(1, number + 1):
#     result *= i

# print(result)
#############################################
# a= [0, 1]
# for i in range(2,10):
#     x = a[i-2]+ a[i-1]
#     a.append(x)
# print(a)

##################################
# x = [[1, 4, 16, 64],[2,3,4, 1],[3, 6, 9, 12]]
# for i in x:
    # y = i[0]
    # for j in i:
    #     if y < j:
    #         y = j
    # print(y)
#######################################
# sort array
# x = [5,3,6,9,8]
# first = 0
# last = len(x) - 1
# while first < last:
#     temp = x[first]
#     x[first]=x[last]    
#     x[last] = temp
#     first += 1
#     last -= 1
# print(x)
#######################################
# rotate 
# x= [1,2,3,4,5]
# d = 2
# k = 0
# temp1 = []
# temp2 = []
# for i in range(0,d):
#     temp1.append(x[i])
# for j in range(d, len(x)):
#     temp2.append(x[j])
# print(temp2 + temp1)
########################################
# write the element without repeat 
# x = [1,277,1,4,1,5,3,4,3,2,1]
# list = []
# for i in x:
#     if i not in list:
#         list.append(i)
#     else:
#         continue
# print(list)
######################################
# just element is not repeated or to remove repeat element
# x = [1,277,1,4,1,5,3,4,3,2,1]
# demo = []
# for i in range(len(x)):
#     if x[i] in demo:
#         demo.remove(x[i])
#     else:
#         demo.append(x[i])
# print(demo)
##################################