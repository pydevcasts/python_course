# mytuple = ("apple", "benana", "cherry")
# print(id(mytuple))
# y = ("melon",)
# print(type(y))
# mytuple = mytuple+y
# print(id(mytuple))

# 140563644762816
# <class 'tuple'>
# 140563644527568
# ===================================
# In [17]: id(x)
# Out[17]: 140475928083264
# In [18]: x.insert(1, 999999)
# In [19]: x
# Out[19]: [1, 999999, 555, 3, 5, 888888]
# In [20]: id(x)
# Out[20]: 140475928083264

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