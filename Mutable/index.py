# mytuple = ("apple", "benana", "cherry")
# print(id(mytuple))
# y = ("melon",)
# print(type(y))
# mytuple = mytuple+y
# print(id(mytuple))

# 140563644762816
# <class 'tuple'>
# 140563644527568
# ====================================
# مرجع قدیمی به سطل اشغال میرود و مرجع جدید مقدار جدید میگیرد
# x = [1,2,3]
# print(id(x))
# print(id(x[0]), id(x[1]), id(x[2]))
# x[0] = 55
# print(id(x[0]), id(x[1]), id(x[2]))
# print(id(x))

# In [17]: id(x)
# Out[17]: 140475928083264
# In [18]: x.insert(1, 999999)
# In [19]: x
# Out[19]: [1, 999999, 555, 3, 5, 888888]
# In [20]: id(x)
# Out[20]: 140475928083264
# # =================================================
# # اما در ایمیوتیبل برعکس
# a = 2
# print(id(2))
# a = 3
# print(id(a))
# ===================================

# ======================================
# thisset = {"apple", "banana", "cherry"}
# print(id(thisset))
# print(thisset + {"kiwi"}) از بیرون ایممیوتیبل
# thisset.update(["orange", "mango", "grapes"]) از درون میوتیبل
# print(id(thisset))
# print(thisset)
# ===================================

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# =============================================
# int, str, float, tuple, frozenset ======> immutable(غیر قابل تغییر)
# dict, list ,set ============>iterable, mutable(قابل تغییر در طول حیات شی)

# Mutable, Iterable = یعنی مرجع قدیمی به سطل اشغال میره و مرجع جدید مقدار جدیدی میگیرد
# Immutable == hashable
# ============================================
# ست ها نامرتبن بنابراین نمیتونیم دو تا ست و با هم جمع کنیم
# میوتیبل باید با میوتیبل جمع بشه 
# تاپل ها ایممیوتیبل هستن بنابراین باید تبدیل به لیستشون کنی تا بتونی بهش اضافه کنی و بعد ای دی بگیری  میبینی که ایدیشون تغییر کرده البته باید دوباره به تاپل برش گردونی بعد ای دی بگیری
# نکته مهم دیگر آن است که لیست‌ها نمی‌توانند عنصر قابل تغییر داشته باشند. بنابراین، در صورتی که دستور {[my_set = {1, 2, [3, 4 از حالت توضیحات خارج و اجرا شود، پیام خطایی به صورت زیر صادر می‌شود.

# unhashable type: 'list

# پس ست ها چون نامنظمند نمیتوان با ست دیگری جمع کرد داخل لیت  ایمیوتیبل و بیرون لیست میوتیبل

# add an element
# my_set.add(2)
# print(my_set)

# add multiple elements
# my_set.update([2,3,4])
# print(my_set)
# Output: {1, 2, 3, 4}

# add list and set
# my_set.update([4,5], {1,6,8})
# print(my_set)
# Output: {1, 2, 3, 4, 5, 6, 8}



# «فروزن‌ست» (Frozenset) یک کلاس جدید است که ویژگی‌های یک مجموعه را دارد،
#  اما عناصر آن پس از تخصیص پیدا کردن قابل تغییر نیستند. 

#  مجموعه‌های غیر قابل تغییر هستند.
#  مجموعه‌های قابل تغییر غیر قابل هش (Hash) شدن هستند،
#  بنابراین نمی‌توان از آن‌ها به عنوان کلیدهای دیکشنری استفاده کرد. از سوی دیگر، 
#  frozenset‌ها قابل هش کردن هستند و می‌توانند به عنوان کلیدهای دیکشنری مورد استفاده قرار بگیرند
#  x = {'text':"salam", {1}:55}

# TypeError: unhashable type: 'set'


# x = {'text':"salam", frozenset("siyamak"):55}

# In [16]: x
# Out[16]: {'text': 'salam', frozenset({'a', 'i', 'k', 'm', 's', 'y'}): 55}

# x = {'text':"salam", [1]:55}

# TypeError: unhashable type: 'list'

# {'text': 'salam', frozenset({'a', 'i', 'k', 'm', 's', 'y'}): 55, (1,): 999}
