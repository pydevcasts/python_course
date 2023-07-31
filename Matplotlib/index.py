import matplotlib.pyplot as plt
import numpy as np
# activities = ['eat', 'sleeps', 'work', 'play'] 
# # portion covered by each label 
# slices = [3, 7, 8, 9] 
# # color for each label 
# colors = ['r', 'y', 'g', 'b'] 
# # plotting the pie chart 
# plt.pie(slices, labels = activities, colors=colors, 
# 		startangle=90, shadow = True, explode = (0, 0.0, 0.1, 0), 
# 		radius = 1.2, autopct = '%1.2f%%') 
# # plotting legend 
# plt.legend() 
# # showing the plot 
# plt.show() 
# # =======================================
# import numpy as np 
# # setting the x - coordinates 
# x = np.arange(0, 2*(np.pi), 0.1)
# print(x) 
# # setting the corresponding y - coordinates 
# y = np.sin(x) 
# # potting the points 
# plt.plot(x, y) 
# # function to show the plot 
# plt.show() 
# ===============================
# import matplotlib.pyplot as plt 
# import numpy as np 
# # # function to generate coordinates 
# def create_plot(ptype): 
# 	# setting the x-axis vaues 
# 	x = np.arange(-10, 10, 0.01) 
# 	# setting the y-axis values 
# 	if ptype == 'linear': 
# 		y = x 
# 	elif ptype == 'quadratic': 
# 		y = x**2
# 	elif ptype == 'cubic': 
# 		y = x**3
# 	elif ptype == 'quartic': 
# 		y = x**4
# 	return(x, y) 
# # setting a style to use 
# plt.style.use('fivethirtyeight') 
# # create a figure 
# fig = plt.figure() 
# # define subplots and their positions in figure 
# plt1 = fig.add_subplot(331) 
# plt2 = fig.add_subplot(332) 
# plt3 = fig.add_subplot(333) 
# plt4 = fig.add_subplot(334) 
# # plotting points on each subplot 
# x, y = create_plot('linear') 
# plt1.plot(x, y, color ='r') 
# plt1.set_title('$y_1 = x$') 
# x, y = create_plot('quadratic') 
# plt2.plot(x, y, color ='b') 
# plt2.set_title('$y_2 = x^2$') 
# x, y = create_plot('cubic') 
# plt3.plot(x, y, color ='g') 
# plt3.set_title('$y_3 = x^3$') 
# x, y = create_plot('quartic') 
# plt4.plot(x, y, color ='k') 
# plt4.set_title('$y_4 = x^4$') 
# # adjusting space between subplots 
# fig.subplots_adjust(hspace=.5,wspace=0.5) 
# # function to show the plot 
# plt.show()
# ================================================
from mpl_toolkits import mplot3d

# x = [1,2,3] 
# # corresponding y axis values 
# y = [2,4,1] 

# plt.plot(x, y, label = "line 1") 


# plt.xlabel('x - axis') 
# plt.ylabel('y - axis') 
# plt.title('My first graph!') 
# plt.show()
# ===============================

# x1 = [1,2,3] 
# y1 = [2,4,1] 
# plt.plot(x1, y1, label = "line 1") 
# x2 = [1,2,3] 
# y2 = [4,1,3] 
# plt.plot(x2, y2, label = "line 2") 
# plt.xlabel('x - axis') 
# plt.ylabel('y - axis') 
# plt.title('Two lines on same graph!') 
# plt.legend() 
# plt.show() 
# # ==========================
# 
# x = [1,2,3,4,5,6] 
# # corresponding y axis values 
# y = [2,4,1,5,2,6] 
# # plotting the points 
# plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
# 		marker='o', markerfacecolor='red', markersize=12) 
# # setting x and y axis range 
# plt.ylim(1,8) 
# plt.xlim(1,8) 
# # naming the x axis 
# plt.xlabel('x - axis') 
# # naming the y axis 
# plt.ylabel('y - axis') 
# # giving a title to my graph 
# plt.title('Some cool customizations!') 
# # function to show the plot 
# plt.show() 
# ======================================
# left = [1, 2, 3, 4, 5]   
# # heights of bars   
# height = [10, 20, 30, 40, 50]   
# # labels for bars   
# tick_label = ['one', 'two', 'three', 'four', 'five']   
# # plotting a bar chart   
# plt.bar(left, height, tick_label = tick_label,   
#         width = 0.18, color = ['blue', 'green', 'red','yellow','black'])   
# # naming the x-axis   
# plt.xlabel('x - axis')   
# # naming the y-axis   
# plt.ylabel('y - axis')   
# # plot title   
# plt.title('bar chart!')   
# # function to show the plot   
# plt.show()
# ====================================
# ages = [2,5,70,40,30,45,50,45,43,40,44,   
#         60,7,13,57,18,90,77,32,21,20,40]   
# # setting the ranges and no. of intervals   
# range = (0, 100)   
# bins = 5  
# # plotting a histogram   
# plt.hist(ages, bins, range, color ='red',   
#         histtype = 'bar', rwidth = 0.8)   
# # x-axis label   
# plt.xlabel('age')   
# # frequency label   
# plt.ylabel('No. of people')   
# # plot title   
# plt.title('My histogram')   
# # function to show the plot   
# plt.show()
# ==================================
# # x-axis values 
# x = [1,2,3,4,5,6,7,8,9,10] 
# # y-axis values 
# y = [2,4,5,7,6,8,9,11,12,12] 
# # plotting points as a scatter plot 
# plt.scatter(x, y, label= "stars", color= "green", 
# 			marker= "*", s=30) 
# # x-axis label 
# plt.xlabel('x - axis') 
# # frequency label 
# plt.ylabel('y - axis') 
# # plot title 
# plt.title('My scatter plot!') 
# # showing legend 
# plt.legend() 
# # function to show the plot 
# plt.show() 
# ================================

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')
# # Data for three-dimensional scattered points
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
# =============================================
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)

Z = f(X, Y)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# ax.view_init(60, 60)
# ================================================
fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.plot_wireframe(X, Y, Z, color='black')
# ax.set_title('wireframe')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')
plt.show()
