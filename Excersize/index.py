
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

# x = ["ali", "siyamak", "mahdi"]
# y = 0
# for i in range(len(x)):
#     while x[y] < x[i]:
#         x[y] = x[y + 1]
#         y +=1
# print(x[y])

# ==================================

# x = ["ali", "siyamak", "mahdi"]
# y = 0
# for i in range(len(x)):
#     if x[y] < x[i]:
#         x[y] = x[y + 1]
  
# print(x[y])
# ====================================
x = [1,2,9,5,8,4,11,33,22,55,999,77]
# y = 0
# for i in range(len(x)):
#     if x[i] > x[y]:
#         x[y] = x[i]
# print(x[y])
# x = [1,2,5,4]

# ========================

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
# ==========================
