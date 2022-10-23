



# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.




# thislist = ["apple", "banana", "cherry"]
# print(thislist * 3)




# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])




# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])




# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])



# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)




# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")



# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))




# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)




# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist) 



# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)



# thislist = ["apple", "banana", "cherry"]
# print(id(thislist))
# mylist = list(thislist)
# print(id(mylist))
# print(mylist)



# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)




# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)



# list1 = ["a", "b" , "c"]
# list2 = [[1, 2, 3], 2]

# list1.extend(list2)
# print(list1)



# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


# ============================
# dir(list)
# 'append', 'clear', 'copy', 'count', 
# 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'