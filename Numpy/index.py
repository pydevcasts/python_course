
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
