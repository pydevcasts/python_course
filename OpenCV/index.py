import matplotlib.pyplot as plt  
# # %matplotlib inline
       
# from skimage import data,filters
       
# image = data.coins()   # ... or any other NumPy array!
# edges = filters.sobel(image)   
# plt.imshow(edges, cmap='gray')
# plt.show()
# =======================================
# import numpy as np
# import matplotlib.pyplot as plt

# from skimage import data
# from skimage.feature import match_template


# image = data.coins()
# coin = image[170:220, 75:130]

# result = match_template(image, coin)
# ij = np.unravel_index(np.argmax(result), result.shape)
# x, y = ij[::-1]

# fig = plt.figure(figsize=(8, 3))
# ax1 = plt.subplot(1, 3, 1)
# ax2 = plt.subplot(1, 3, 2)
# ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

# ax1.imshow(coin, cmap=plt.cm.gray)
# ax1.set_axis_off()
# ax1.set_title('template')

# ax2.imshow(image, cmap=plt.cm.gray)
# ax2.set_axis_off()
# ax2.set_title('image')
# # highlight matched region
# hcoin, wcoin = coin.shape
# rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
# ax2.add_patch(rect)

# ax3.imshow(result)
# ax3.set_axis_off()
# ax3.set_title('`match_template`\nresult')
# # highlight matched region
# # ax3.autoscale(False)
# ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

# plt.show()
# ======================================
import numpy as np
# from skimage import data
import matplotlib.pyplot as plt
# # %matplotlib inline
   
# image = data.camera()  
# type(image)
# # numpy.ndarray #Image is a NumPy array: 

# mask = image < 87  
# image[mask]=25 
# plt.imshow(image, cmap='gray')
# plt.show()
# ===================================
from scipy.ndimage import gaussian_filter
from scipy import misc

# a = np.arange(50, step=2).reshape((5,5))
# # gaussian_filter(a, sigma=1)

# fig = plt.figure()
# plt.gray()  # show the filtered result in grayscale
# ax1 = fig.add_subplot(121)  # left side
# ax2 = fig.add_subplot(122)  # right side
# ascent = misc.ascent()
# result = gaussian_filter(ascent, sigma=5)
# ax1.imshow(ascent)
# ax2.imshow(result)
# plt.show()
# ================================
# from scipy import ndimage, misc
# import matplotlib.pyplot as plt
# fig = plt.figure()
# plt.gray()  # show the filtered result in grayscale
# ax1 = fig.add_subplot(121)  # left side
# ax2 = fig.add_subplot(122)  # right side
# ascent = misc.ascent()
# result = ndimage.prewitt(ascent)
# ax1.imshow(ascent)
# ax2.imshow(result)
# plt.show()
# ======================================
# from scipy import ndimage, misc
# import matplotlib.pyplot as plt
# fig = plt.figure()
# plt.gray()  # show the filtered result in grayscale
# ax1 = fig.add_subplot(121)  # left side
# ax2 = fig.add_subplot(122)  # right side
# ascent = misc.ascent()
# result = ndimage.sobel(ascent)
# ax1.imshow(ascent)
# ax2.imshow(result)
# plt.show()
# ===================================
# from PIL import Image,ImageFilter  
# #Read image
# im = Image.open("/home/siyamak/Pictures/Image-Processing-Python-Fig04.png.webp")
# #Display image  
# im.show()
   
# from PIL import ImageEnhance  
# enh = ImageEnhance.Contrast(im)  
# enh.enhance(1.8).show("30% more contrast")
# ====================================
# import cv2
# gray_img = cv2.imread('/home/siyamak/Pictures/Image-Processing-Python-Fig04.png.webp', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Grayscale', gray_img)
# cv2.waitKey()
# cv2.imwrite('watchgray.webp', gray_img)
# cv2.waitKey()
# ===================================
import cv2
import numpy as np,sys

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)