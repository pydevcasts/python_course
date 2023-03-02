# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)
# ===============================


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["year"] = 2018

# print(thisdict)
# ===================================

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)
# ====================================

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])
# ===============================


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)
# ================================


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(len(thisdict))
# ================================

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# ====================================

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("brand") required to be having a argument but in list is not nessery istead we run popitem()
# print(thisdict)
# =======================================

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)
# ===================================

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)
# =====================================

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict == thisdict)
# =================================

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict is thisdict)
# =====================================

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily)
# ========================================

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)
# =======================================

# thisdict = dict(brand="Ford", model="Mustang", year=1964)
# print(thisdict)


# ========================================

# dict1 = {"key1":1, "key2":2}
# dict2 = {"key2":2, "key1":1}
# print(dict1 == dict2)
# ===============================
# Dictionary keys must be immutable

# True
# False
# ==============================
# Select the all correct way to remove the key marks from a dictionary
# student = { 
#   "name": "Emma", 
#   "class": 9, 
#   "marks": 75 
# }

# 1-student.pop("marks")
# 2 -del student["marks"]
# 3 -student.remove("marks")
# 4 -student.popitem("marks")

# ==================================
# . Please select all correct ways to empty the following dictionary
# student = { 
#   "name": "Emma", 
#   "class": 9, 
#   "marks": 75 
# }
# del student
# del student[0:2]
# student.clear()
# =============================================
# dictionary comperehentions
# letter = ["a", "b", "c"]
# arr = [1,2,3]
# print({key.upper():value for key, value in zip(letter, arr)})