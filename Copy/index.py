import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1) #shallowcopy
print ("The original elements before deep copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")
li2[2][0] = 7
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
	print (li2[i],end=" ")

print("\r")
print ("The original elements after deep copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")
####################################################
import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
print ("The original elements before deep copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")
li2[2][0] = 7
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
	print (li2[i],end=" ")

print("\r")
print ("The original elements after deep copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")
