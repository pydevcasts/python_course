#sets is  iterable 

# ===================================
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# ======================================

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# ==============================

# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

# =================================

# dir(set)
# 'clear', 'copy', 'pop', 'remove', 'union', 'update', 'discard

# ======================================

# thisset = {"apple", "banana", "cherry"}
# print(id(thisset))
# print(thisset + {"kiwi"})
# thisset.update(["orange", "mango", "grapes"])
# print(id(thisset))
# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# ===============================

# Kelidestan_Set = {10, 10, 10, 11, 11, 11, 11, 12, 12}
# print(len(Kelidestan_Set))

# ==================================

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("kiwi")
# print(thisset)

# =================================

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("kiwi")
# print(thisset)

# ===============================
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# =================================

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# ===============================
# x = "mahdy pythonist"
# print(set(x))
# out:
# {'n', 'i', ' ', 'a', 'p', 'd', 'y', 'm', 's', 'o', 'h', 't'}
# ================================
# x = {1,2,5,9}
# x.add(225)
# print(x)
# ==============================


# a = {1,2,5}
# b = {4,8,2,9}
# # print(a.union(b)) a + b
# print(a | b)
# ======================
# print(a.difference(b)) 
# print(a.intersection(b))


# =================================
# تغییر آیتم های مجموعه ست

# زمانی که یک ست ایجاد می شود، نمی توان عناصرش را تغییر داد ولی می توان عناصر را به آنها اضافه کرد

# اضافه کردن آیتم به مجموعه ست

# برای اضافه کردن عنصر به مجموعه ست ، باید از تابع ()Add استفاده کنید

# برای اینکه بتوانید بیشتر از یک عنصر به مجموعه ست اضافه کنید باید از تابع ()update اسنتفاده کنید

# در صورتیکه محدوده ایندکس خود را بدون ایندکس شروع رها کنید، ایندکس شروع شما، ایندکس ابتدای لیست  یا ایندکس صفر می باشد.

# نکته مهم دیگر آن است که لیست‌ها نمی‌توانند عنصر قابل تغییر داشته باشند. بنابراین، در صورتی که دستور {[my_set = {1, 2, [3, 4 از حالت توضیحات خارج و اجرا شود، پیام خطایی به صورت زیر صادر می‌شود.

# unhashable type: 'list