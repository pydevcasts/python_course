

# 🐍 **فصل ۱: شروع ماجراجویی با پایتون**

## ✨ صفحه ۳: آشنایی با متغیرها و انواع داده‌ها در پایتون 💡

خب تا الان پایتون و VS Code رو نصب کردی، کد چاپ نوشتی، ورودی گرفتی و حتی با شرط‌ها بازی کردی 🎉
اما حالا وقتشه بفهمیم پشت صحنه‌ی این همه داده و مقدار چی می‌گذره!

---

## 🧠 متغیر یعنی چی؟

متغیر یا **Variable** مثل یه جعبه‌ست که داخلش چیزی نگه می‌داری.
هر جعبه یه اسم داره و می‌تونه هر چیزی داخلش باشه: عدد، متن، یا حتی یه مقدار منطقی (درست یا غلط).

📦 مثال ساده:

```python
# Variable examples
name = "Siamak"     # string (رشته)
age = 25            # integer (عدد صحیح)
height = 1.80       # float (عدد اعشاری)
is_student = True   # boolean (درست یا غلط)
```

در واقع وقتی این کد رو اجرا می‌کنی، پایتون در حافظه برای هر اسم (مثل name، age) یه بخش کوچیک می‌سازه تا مقدارش رو نگه داره.

---

## 🎨 انواع داده‌های اصلی (Built-in Data Types)

پایتون چند نوع داده‌ی پایه داره که همیشه باهاشون سروکار داری:

| نوع داده | مثال                | توضیح فارسی |
| -------- | ------------------- | ----------- |
| `int`    | `10, -5, 1000`      | عدد صحیح    |
| `float`  | `3.14, -0.5`        | عدد اعشاری  |
| `str`    | `"Python", 'Hello'` | رشته (متن)  |
| `bool`   | `True, False`       | درست یا غلط |

---

## 🔍 چطور بفهمیم نوع یه داده چیه؟

با تابع `type()` خیلی راحت می‌فهمی نوع متغیر چیه 👇

```python
# Checking data types
x = 10
y = 3.14
z = "Python"
t = True

print(type(x))
print(type(y))
print(type(z))
print(type(t))
```

📤 خروجی:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

پایتون بهت می‌گه هر کدوم از چه نوعیه.

---

## 🧮 تبدیل نوع داده‌ها (Type Casting)

گاهی لازمه نوع داده‌هارو تغییر بدی. مثلاً وقتی با ورودی کاربر (`input()`) سر و کار داری، همیشه خروجی رشته‌ست.
اگه بخوای با اون عدد جمع بزنی، باید تبدیلش کنی به عدد 👇

```python
# Type conversion
age = input("Enter your age: ")   # always string
age = int(age)                    # convert to integer

print("Next year you'll be:", age + 1)
```

📤 خروجی:

```
Enter your age: 25
Next year you'll be: 26
```

اگر تبدیل نکنی، خطا می‌گیری چون پایتون نمی‌تونه رشته رو با عدد جمع بزنه 😅

---

## 💬 رشته‌ها (Strings) — بازی با متن‌ها 🎭

رشته یعنی هر چیزی که داخل گیومه (' ') یا (" ") قرار بگیره.
مثلاً `"Hello"` یا `'Python'`.

می‌تونی رشته‌ها رو به هم بچسبونی یا حتی تکرارشون کنی:

```python
# String examples
first = "Python"
last = "Rules!"
message = first + " " + last
print(message)

echo = "Ha " * 3
print(echo)
```

📤 خروجی:

```
Python Rules!
Ha Ha Ha 
```

---

## 🧠 تمرین ذهنی: تفاوت int و str

به این کد نگاه کن 👀👇

```python
a = "5"
b = 5

print(a * 3)
print(b * 3)
```

خروجی چیه؟ 😏

🔹 چون `a` یه رشته‌ست، خروجی: `"555"`
🔹 چون `b` یه عدد صحیحه، خروجی: `15`

همین تفاوت‌های کوچیکه که باید حواست بهش باشه!

---

## 🧩 کار با Boolean (درست یا غلط)

متغیرهای بولی برای تصمیم‌گیری و شرط‌ها عالی‌ان.
اون‌ها فقط دو حالت دارن: `True` یا `False`

```python
# Boolean example
is_raining = False
is_sunny = True

print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)
```

📤 خروجی:

```
Is it raining? False
Is it sunny? True
```

می‌تونی با این‌ها توی شرط‌ها و حلقه‌ها تصمیم بگیری چه کاری انجام بشه.

---

## 💪 تمرین عملی — تمرین شماره ۱

یه فایل جدید به اسم `variables_practice.py` بساز و داخلش بنویس 👇

```python
# Variable practice exercise

# 1️⃣ Ask for user info
name = input("What's your name? ")
age = int(input("How old are you? "))
city = input("Where do you live? ")

# 2️⃣ Calculate something
next_year_age = age + 1

# 3️⃣ Print a friendly summary
print(f"Hey {name}! You're from {city}, right?")
print(f"Next year, you'll be {next_year_age}! 🎉")

# 4️⃣ Check if user is adult
is_adult = age >= 18
print("Are you an adult?", is_adult)
```

📤 مثال خروجی:

```
What's your name? Sara
How old are you? 20
Where do you live? Tehran
Hey Sara! You're from Tehran, right?
Next year, you'll be 21! 🎉
Are you an adult? True
```

---

## 🧡 نکات طلایی این صفحه:

✅ متغیر = جعبه‌ای برای نگهداری داده
✅ انواع داده‌ی پایه: `int`, `float`, `str`, `bool`
✅ با `type()` می‌فهمی نوع داده چیه
✅ با `int()`, `str()`, `float()` می‌تونی تبدیلشون کنی
✅ رشته‌ها و بولین‌ها ابزارهای پرکاربرد در پایتون هستن
✅ تمرین باعث میشه مغزت با منطق پایتون یکی بشه 🤯💪

---
> «برو صفحه ۴»
