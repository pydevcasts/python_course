
# 🐍 **فصل ۱: شروع ماجراجویی با پایتون**

## ✨ صفحه ۴: ورودی و خروجی در پایتون — صحبت با کاربر 🎤💬

خب تا حالا یاد گرفتی متغیر چیه، چطور مقدار ذخیره می‌کنی و انواع داده‌ها (عدد، رشته، بولین) چیا هستن.
اما برنامه بدون ارتباط با کاربر خیلی بی‌روح میشه 😅
پس حالا وقتشه یاد بگیری **چطور از کاربر اطلاعات بگیری (input)** و **چطور نتیجه رو نشون بدی (print)** — درست مثل گفت‌وگو بین انسان و کامپیوتر 🤝💻

---

## 🧠 مفهوم ورودی و خروجی

🟢 **ورودی (Input):** یعنی داده‌هایی که کاربر وارد برنامه می‌کنه.
🔵 **خروجی (Output):** یعنی چیزهایی که برنامه به کاربر نشون می‌ده.

در پایتون دو تابع خیلی مهم برای این کار داریم:

* `input()` برای دریافت اطلاعات
* `print()` برای نمایش اطلاعات

---

## 💬 تابع input() — دریافت داده از کاربر

```python
# Asking for input
name = input("What's your name? ✨: ")
print("Nice to meet you,", name, "😄!")
```

📤 خروجی:

```
What's your name? ✨: Siamak
Nice to meet you, Siamak 😄!
```

نکته: خروجی تابع `input()` همیشه از نوع **string** هست حتی اگه عدد وارد کنی!

---

## 🔢 تبدیل ورودی‌ها به عدد

اگر از کاربر عدد می‌خوای و قراره باهاش محاسبه انجام بدی، باید اون ورودی رو تبدیل به عدد (`int` یا `float`) کنی 👇

```python
# Numeric input
age = int(input("How old are you? 🎂: "))
next_year = age + 1
print("Next year you'll be", next_year, "years old! 🎉")
```

📤 خروجی:

```
How old are you? 🎂: 25
Next year you'll be 26 years old! 🎉
```

---

## 🖨️ تابع print() — نمایش داده‌ها به کاربر

تابع `print()` وظیفه داره هر چیزی داخلش بنویسی، روی صفحه نشون بده.
می‌تونه متن، عدد، یا ترکیب هر دو باشه.

```python
# Simple prints
print("Python is fun! 🐍")
print("2 + 2 =", 2 + 2)
```

📤 خروجی:

```
Python is fun! 🐍
2 + 2 = 4
```

---

## 🎨 قالب‌بندی خروجی‌ها — زیبا نوشتن متن‌ها

راه‌های مختلفی برای ترکیب متن و متغیر در پایتون هست.
بیاین با هم ببینیم:

### 1️⃣ روش کلاسیک با ویرگول

```python
name = "Sara"
print("Hello", name, "welcome to Python! 😍")
```

📤 خروجی:
`Hello Sara welcome to Python! 😍`

---

### 2️⃣ روش با + (ترکیب رشته‌ها)

```python
print("Hello " + name + " welcome to Python! 🐍")
```

📤 خروجی:
`Hello Sara welcome to Python! 🐍`

💡 فقط یادت باشه در این روش باید همه چیز از نوع رشته باشه.

---

### 3️⃣ روش حرفه‌ای‌تر: **f-String** 💎

(از نسخه 3.6 به بعد پایتون)

```python
age = 20
print(f"Hello {name}! Next year you'll be {age + 1} 🎂")
```

📤 خروجی:
`Hello Sara! Next year you'll be 21 🎂`

این روش خواناتر، سریع‌تر و استانداردتره — پس همیشه پیشنهاد می‌شه ازش استفاده کنی 😉

---

## 🧮 چند مثال ترکیبی جذاب

### 🎵 مثال ۱: سلام دوستانه

```python
# Friendly greeting program
name = input("Enter your name: ")
mood = input("How are you feeling today? 😊: ")

print(f"Hey {name}! Glad to hear you're feeling {mood} today! 🌈")
```

---

### 📊 مثال ۲: جمع دو عدد از ورودی

```python
# Add two numbers entered by the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2
print(f"The sum of {num1} and {num2} is {result} 🧮")
```

📤 خروجی نمونه:

```
Enter first number: 4
Enter second number: 5
The sum of 4.0 and 5.0 is 9.0 🧮
```

---

## 🎯 نکته حرفه‌ای: پارامتر sep و end در print

تابع `print()` دو گزینه جالب داره که کمتر کسی استفاده می‌کنه ولی خیلی کاربردیه 👇

```python
print("A", "B", "C", sep="-")
```

📤 خروجی:

```
A-B-C
```

و پارامتر `end` برای کنترل انتهای چاپ (پیش‌فرض \n یعنی خط جدید) 👇

```python
print("Loading", end="...")
print("Done! ✅")
```

📤 خروجی:

```
Loading...Done! ✅
```

---

## 🧠 تمرین شماره ۲

یه فایل جدید بساز به اسم `user_info.py` و داخلش بنویس 👇

```python
# A small user profile generator
name = input("What's your name? ")
age = int(input("How old are you? "))
hobby = input("What's your favorite hobby? 🎨: ")

print(f"Hello {name}! 👋")
print(f"You are {age} years old and you love {hobby}! ❤️")
print(f"Next year you'll be {age + 1}! Keep learning Python 🐍!")
```

📤 خروجی نمونه:

```
What's your name? Reza
How old are you? 19
What's your favorite hobby? 🎨: Painting
Hello Reza! 👋
You are 19 years old and you love Painting! ❤️
Next year you'll be 20! Keep learning Python 🐍!
```

---

## 💎 نکات طلایی این صفحه:

✅ با`input()` برای دریافت اطلاعات از کاربر

✅ با `print()` برای نمایش نتیجه

✅ همیشه یادت باشه ورودی رشته‌ست، اگر عدد خواستی باید تبدیلش کنی

✅ با `f-string` می‌تونی متن‌هات رو قشنگ و تمیز چاپ کنی

✅ با `sep` و `end` خروجی‌هات رو حرفه‌ای‌تر کن

---

> «برو صفحه ۵»
