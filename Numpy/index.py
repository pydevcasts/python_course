
# ===================================
# import numpy as np 
# import matplotlib.pyplot as plt 
# # x co-ordinates 
# x = np.arange(0, 9) 
# A = np.array([x, np.ones(9)]) 
# # linearly generated sequence 
# y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24] 
# # obtaining the parameters of regression line 
# w = np.linalg.lstsq(A.T, y)[0]  
# # plotting the line 
# line = w[0]*x + w[1] # regression line 
# plt.plot(x, line, 'r-') 
# plt.plot(x, y, 'o') 
# plt.show()
# =================================
# import numpy as np
# A = np.matrix(np.ones((4,4)))
# np.array(A)[2]=2
# print(A)
# np.asarray(A)[2]=2
# print(A)
# =================
# import py_compile
# import os
# x = py_compile.compile('Numpy/demo.txt')
# print(x)
# =======================
# with open('Numpy/demo.txt', 'rb') as f:
#     s = f.read()
#     print(s)
# s.find(b'\xff\xc0')
# print(s)
# ================
import string

import numpy as np

# x = np.array([[1, 1],[2, 2], [3,3]])
# print(x[:1])

# ================================
# importing required packages

# import time

# # size of arrays and lists
# size = 1000000

# # declaring lists
# list1 = range(size)
# list2 = range(size)

# # declaring arrays
# array1 = numpy.arange(size)
# array2 = numpy.arange(size)

# # list
# initialTime = time.time()
# resultantList = [(a * b) for a, b in zip(list1, list2)]

# # calculating execution time
# print("Time taken by Lists :",
# 	(time.time() - initialTime),
# 	"seconds")

# # NumPy array
# initialTime = time.time()
# resultantArray = array1 * array2

# # calculating execution time
# print("Time taken by NumPy Arrays :",
# 	(time.time() - initialTime),
# 	"seconds")
# ==============================
# x = [1,2,3]
# arr = np.array(x)
# print(arr)
# =======================
# print(np.zeros(5))
# ==========================
# print(np.arange(100))
# =========================
# arr = np.logspace(0,1, 100, base = 10.0)
# print(arr)
# =========================
# print(np.zeros((5,5)))
# ============================
# cube = np.zeros((5,5,5)).astype(int) + 1
# print(cube)
# =======================
# cube = np.ones((5,5,5)).astype(np.float16)
# print(cube)
# ===========================
# print(np.zeros(2, dtype = (int)))
# print(np.zeros(2, dtype = np.float32))
# =====================================
# print(np.arange(1000))
# print(np.arange(1000).reshape((10,10,10)))
# =======================================
# recarr = np.zeros((2,), dtype = ('i4,f4,a10'))
# toadd = [(1,2.,'hello'), (2,3.,'world')]
# # print(toadd)
# recarr[:] = toadd
# print(recarr)
# ===========================================
# x = np.zeros((2,), dtype =('i4,f4,a10'))
# y = np.arange(2) + 1
# z = np.arange(2,dtype=(np.float32))
# h = ['hello', 'world']
# print(x)
# print(y)
# print(z)
# toadd = zip(y,z,h)
# x[:] = list(toadd)
# print(x[:])
# =====================================
# x = [[1,2],[3,4]]
# # print(x[0][1])
# arr =np.array(x)
# print(arr[0,1])
# print(arr[:,1])
# print(arr)
# ====================================
# arr = np.arange(5)
# print(arr)
# print(np.delete(arr, np.where(arr > 2)))
# ==================================
# img1 = np.zeros((20,20)) + 3
# img1[4:-4, 4:-4] = 6
# print(img1)
# =====================================
# arr = np.loadtxt('demo.txt', dtype={'name':('ID','Result','Type'), 'formats':('S4','f4','i2')})
# arr = np.savetxt('demoone.txt', 2)
# print(arr)
# ====================================
# data = np.zeros((2,2))
# print(data)
# print(np.save('test.npy',data))
# print(np.load('test.npy'))
# ============================
# A = np.array( [[1,1],[0,1]] )
# B = np.array( [[2,0],[3,4]] )
# # print(A*B) # ضرب در سطح عناصر

# print(np.dot(A,B)) # ضرب در سطح ماتریس
# ==============================
# def f(x,y):
#     return 10*x+y

# b = np.fromfunction(f,(5,4),dtype=int)
# # print(b[1,])
# print(np.vstack(b))
# =========================
# import numpy as np 
# a = np.array([[1, 2], 
#               [3, 4]]) 
# b = np.array([[5, 6], 
#               [7, 8]]) 
# vertical stacking 
# print("Vertical stacking:\n", np.vstack((a, b))) 
# horizontal stacking 
# # print("\nHorizontal stacking:\n", np.hstack((a, b))) 
# c = [5, 6] 
# # # stacking columns 
# print("\nColumn stacking:\n", np.column_stack((a, c))) 
# # concatenation method  
# print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1)) 
# =============================================================
# import numpy as np 
# a = np.array([[1, 3, 5, 7, 9, 11], 
#               [2, 4, 6, 8, 10, 12]]) 
# # horizontal splitting 
# print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 2)) 
# # vertical splitting 
# print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(a, 2))
# ======================================
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)
# import numpy as np
# e  = np.array([(1,2,3), (4,5,6)])
# print(e[:,1])


char_ints = [ord(c) for c in string.ascii_letters]

with open("demo.txt", "wb") as fo:
    with open("demo.txt", "rb") as fi:

        # Read bytes but only keep letters.
        chars = []
        for b in fi.read():
            if b in char_ints:
                chars.append(chr(b))
            else:
                chars.append(" ")

        # Search for 'ABC' in the read letters.
        pos = "".join(chars).index("ABC")

        # We now know the position of the intersting byte.
        pos_x = pos + len("ABC") + 3 # known offset

        # Now copy all bytes from the input to the output, ...
        fi.seek(0)
        i = 0
        for b in fi.read():
            # ... but replace the intersting byte.
            if i == pos_x:
                fo.write(b"Y")
            else:
                fo.write(bytes([b]))
            i = i + 1
##################################################################
import sys
import numpy as np
import time
import matplotlib.pyplot as plt



l  = np.array((1, 8 , 9))
print(l)
x = np.array((44,55,88,77,99,555,444,888,999,))
g = np.array([
    (1, 2, 4),
    (4, 8, 9),
    (7, 8, 5),

]
)
print(np.array(g).ndim)
print(np.array(x).ndim)
print(np.array(l).ndim)


print(np.array(l).dtype)
print(np.array(x).dtype)
print(np.array(g).dtype)


# linspace: با دادن حد بالا، حد پایین و تعداد اعداد، یک ترکیب خطی از اعدادِ بین دو حد، ایجاد می‌کند.
u  = np.linspace(1, 8 , 9)
print(u)



# plt.plot(l)
# plt.show()

# ones: به ابعاد دلخواه ۱ ایجاد می‌کند.

p = np.ones((3,4))
print(p)

# zeros: به ابعاد دلخواه ۰ ایجاد می‌کند.

k= np.zeros((3,4))
print(k)

f = np.random.random((6,8))
print(f)


# متد normal، توزیع نرمالی از اعداد تصادفی ‌تولید می‌کند. این متد ۳ پارامتر اصلی می‌پذیرد: میانگین، انحراف معیار و تعداد داده‌ها


m = np.random.normal((20,10,1000))
print(m)

plt.scatter(m,np.arange(1,len(m)+1,1),color="cyan")
plt.show()
plt.plot(m,color="red")

# full: آرایه‌ را با یک مقدار به ابعاد دلخواه پر می‌کند.
c = np.full((4,2), 5.45)
plt.plot(c,color="black")
plt.show()
# print(c)

# numpy از توابع مختلفی پشتیبانی می‌کند. برای مثال تابع سینوس به صورت زیر است:
d = np.arange(0,3*np.pi,0.1)
y = np.sin(d)
plt.plot(y, linewidth=10, color="green")
plt.show()