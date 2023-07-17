#sets is  iterable 

# ===================================
# thisset = {"apple", "banana", "cherry", "banana"} #no duplicated
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
# thisset.add("blueberry")
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
# 
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
# print(elahe)

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


a = {1,2,5}
b = {4,8,2,9}
# print(a + b)#error
# print(a.union(b)) #a + b
# print(a | b)
# print(a.difference(b)) 
# print(a.intersection(b))
# ======================


# =================================
# تغییر آیتم های مجموعه ست

# زمانی که یک ست ایجاد می شود، نمی توان عناصرش را تغییر داد ولی می توان عناصر را به آنها اضافه کرد

# اضافه کردن آیتم به مجموعه ست

# برای اضافه کردن عنصر به مجموعه ست ، باید از تابع ()Add استفاده کنید

# برای اینکه بتوانید بیشتر از یک عنصر به مجموعه ست اضافه کنید باید از تابع ()update اسنتفاده کنید

# نکته مهم دیگر آن است که ستها نمی‌توانند عنصر قابل تغییر داشته باشند. بنابراین، در صورتی که دستور {[my_set = {1, 2, [3, 4 از حالت توضیحات خارج و اجرا شود، پیام خطایی به صورت زیر صادر می‌شود.

# unhashable type: 'list
# تفاوت ست و فروزن ست فقط اینه که فروزن ستها هشبل هستند و میتونند به ست و دیکشنری اضافه بشن
# ووجه مشترک ایتریبل و ایممیوتیبل هستند

# x = {1,2,frozenset(222), 5}
# x = {1:2222,2:22,set("222"):88, 5:77}
# print(x)

# x = {"name":"zahra", 1:2, frozenset([1]):"heydari"} #unmutabel, hashble
# print(x)

# x = {1,2}
# print(type(x))
# y = frozenset(["elahe"])
# print(type(y))
# =============================
