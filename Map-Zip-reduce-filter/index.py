x = [1,12,3]
y = [1,17,13]

z = list(map(lambda x, y:x-y, x, y))
print(z)
##############################################
arr = [2,5,6,9,8,4,1,11,44,15,18,16]

mylist = list(filter(lambda x:x > 10, x))
print(mylist)
###############################################
from  functools import reduce
arr = [2,5,6,9,8,4,1,11,44,15,18,16]

sum = reduce(lambda x, y:x+y, arr)
print(sum)
############################################
import operator 
lis = [1, 3, 5, 6, 2] 
print(reduce(operator.add, lis)) 
print(reduce(operator.mul, lis)) 
print(reduce(operator.add, ["geeks", "for", "geeks"])) 
###########################################################
lis = [1, 3, 5, 6, 2] 
mis="siyamak"
z = [{i:j} for i , j in zip(mis, lis)]
print(z)
####################################################
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
mapped = zip(name, roll_no)
print(set(mapped))
#######################################################

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

z = zip(names, ages)
print(set(z))
###########################################################
names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
	print(i, name, age)


