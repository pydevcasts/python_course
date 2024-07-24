import numpy as np

# x = np.array([1,2,3,4])
# print(x[np.newaxis,:])
# print(x.shape)
# print(x.dtype)

################################
# c = np.array([(1,2,3),
#               (4,5,6)])
# print(c.shape)
# print(c.dtype)
################################
# a = np.array([0.0, 10.0, 20.0, 30.0]) 
# b = np.array([0.0, 1.0, 2.0, 5.1]) 
# print(a[:, np.newaxis] + b)
####################################
# d = np.array([
#                 [[1, 2,3],
#                 [4, 5, 6]],
#                 [[7, 8,9],
#                 [10, 11, 12]]
# ],dtype=np.complex128)
# print(d.itemsize)
################################################
# x = np.array([1,2,3], dtype=np.complex128)
# print(x.itemsize)
###############################################
# np.zeros((2,2))
# #Example numpy zero with datatype
# print(np.zeros((2,2), dtype=np.int16))
# #Example numpy one 2D Array with datatype
# print(np.ones((2,2,3), dtype=np.int64))
##############################################
# e  = np.array([(1,2,3), (4,5,6)])
# print(e.reshape(3,2))
###############################################
# یک آرایه دو بعدی
# x = np.array([[1, 2, 3], [4, 5, 6]])
# print(x.flatten())  # خروجی: [1 2 3 4 5 6]
###############################################
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# داده‌های نمونه
# ویژگی‌ها (X) و اهداف (y)
X = np.array([[1], [2], [3], [4], [5]])  # ویژگی‌ها
y = np.array([1, 2, 3, 4, 5])            # اهداف

# ایجاد مدل رگرسیون خطی
model = LinearRegression()

# آموزش مدل
model.fit(X, y)

# پیش‌بینی با استفاده از داده‌های ورودی
X_new = np.array([[6], [7]])
y_pred = model.predict(X_new)

# نمایش نتایج
print("پیش‌بینی‌ها:", y_pred)

# رسم نتایج
plt.scatter(X, y, color='blue', label='داده‌های واقعی')
plt.plot(X_new, y_pred, color='red', label='پیش‌بینی')
plt.xlabel('ویژگی‌ها')
plt.ylabel('اهداف')
plt.title('رگرسیون خطی ساده')
plt.legend()
plt.show()
#################################################################
# داده‌های نمونه: ساعت‌های مطالعه و نمره‌ها
X = np.array([1, 2, 3, 4, 5])  # ساعت‌های مطالعه
y = np.array([2, 4, 5, 4, 5])  # نمره‌ها
# تعداد داده‌ها
N = len(X)

# محاسبه m و b
m = (N * np.sum(X * y) - np.sum(X) * np.sum(y)) / (N * np.sum(X**2) - (np.sum(X))**2)
b = (np.sum(y) - m * np.sum(X)) / N

print(f"ضریب (m): {m}, عرض از مبدأ (b): {b}")
# پیش‌بینی نمره برای ساعت مطالعه 6
hours_studied = 6
predicted_score = m * hours_studied + b
print(f"پیش‌بینی نمره برای {hours_studied} ساعت مطالعه: {predicted_score}")
###############################################
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# داده‌های نمونه
# x به عنوان ویژگی (feature) و y به عنوان هدف (target)
x = np.array([[1], [2], [3], [4], [5], [6]])  # ویژگی‌ها
y = np.array([1, 2, 3, 4, 5, 6])              # اهداف

# تقسیم داده‌ها به مجموعه‌های آموزش و تست
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# ایجاد مدل رگرسیون خطی
model = LinearRegression()

# آموزش مدل
model.fit(x_train, y_train)

# پیش‌بینی با استفاده از داده‌های تست
y_pred = model.predict(x_test)

# نمایش نتایج
print("پیش‌بینی‌ها:", y_pred)
print("واقعیت‌ها:", y_test)

# رسم نتایج
plt.scatter(x, y, color='blue', label='داده‌های واقعی')
plt.plot(x_test, y_pred, color='red', label='خط رگرسیون')
plt.xlabel('ویژگی‌ها')
plt.ylabel('اهداف')
plt.title('رگرسیون خطی')
plt.legend()
plt.show()
