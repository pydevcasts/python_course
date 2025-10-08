
# 🐍 **فصل ۲: تصمیم‌گیری و تکرار در پایتون**

## ✨ صفحه ۲ — آشنایی با حلقه‌ while 🔁

خب سیامک، تا اینجا یاد گرفتی چطور با `if` و `else` تصمیم بگیری.
ولی حالا وقتشه یاد بگیری **چطور کاری رو چند بار تکرار کنی** —
چیزی که در برنامه‌نویسی بهش می‌گن **حلقه (Loop)** 🔄

---

## 🎯 مفهوم حلقه

گاهی وقتا لازم داری یه دستور چند بار پشت‌سر‌هم اجرا بشه.
مثلاً بخوای عددها رو یکی‌یکی چاپ کنی یا از کاربر چند بار ورودی بگیری.
به جای اینکه ۱۰ بار بنویسی `print(...)`، از **حلقه‌ها** استفاده می‌کنی تا این کار خودکار تکرار بشه. 😄

---

## 🔹 حلقه‌ی `while` چیه؟

کلمه‌ی کلیدی `while` یعنی:
“**تا وقتی که شرط درست باشه، این کد رو تکرار کن.**”

فرمولش اینطوریه 👇

```python
while condition:
    # code block to repeat
```

وقتی شرط False بشه، حلقه متوقف می‌شه.

---

## 🧩 مثال ۱: شمارش از ۱ تا ۵

بیایم با یه مثال خیلی ساده شروع کنیم 👇

```python
i = 1  # starting point

while i <= 5:
    print(i)
    i += 1  # increase i by 1 each loop
```

📤 خروجی:

```
1
2
3
4
5
```

🔍 توضیح:

* اول `i = 1`
* تا وقتی `i <= 5` باشه، چاپ می‌کنه
* هر بار یکی زیادش می‌کنیم (`i += 1`)
* وقتی `i` بشه ۶، شرط دیگه درست نیست و حلقه تموم می‌شه.

---

## ⚠️ نکته مهم — خطر حلقه‌ی بی‌نهایت 😱

اگه مقدار متغیر داخل شرط رو تغییر ندی، حلقه هیچ‌وقت تموم نمی‌شه!

```python
# Infinite loop example 😅
i = 1
while i <= 5:
    print(i)
    # forgot i += 1
```

این برنامه تا ابد عدد 1 رو چاپ می‌کنه!
همیشه حواست باشه که شرط حلقه **یه‌جایی False بشه** تا حلقه تموم بشه ✅

---

## 🧩 مثال ۲: شمارش معکوس

بیایم برعکسش کنیم 👇

```python
count = 5

while count > 0:
    print(count)
    count -= 1  # decrease count by 1

print("Boom! 💥")
```

📤 خروجی:

```
5
4
3
2
1
Boom! 💥
```

---

## 💬 مثال ۳: پرسیدن تا جواب درست بدی

گاهی برنامه باید تا زمانی که کاربر پاسخ درستی بده، تکرار بشه.

```python
# Repeat until user types 'python'
word = ""

while word != "python":
    word = input("What is my favorite programming language? 🤔: ")

print("Well done! 🎉 That's the correct answer! 🐍")
```

📤 نمونه اجرا:

```
"What is my favorite programming language? 🤔:"java
“What is my favorite programming language? 🤔:"c++
“What is my favorite programming language? 🤔:" python
“Well done! 🎉 That’s the correct answer! 🐍”
```

---

## 🧠 نکته حرفه‌ای: استفاده از `break` برای خروج زودتر

اگر بخوای وسط حلقه، در شرایط خاصی **خارج بشی**، از دستور `break` استفاده کن.

```python
while True:
    name = input("Please enter your name (type 'exit' to quit): ")  # Prompt the user for their name
    if name == "exit":  # Check if the user wants to exit
        print("Exiting the program 👋")  # Print exit message
        break  # Exit the loop
    print(f"Hello {name}! 😊")  # Greet the user with their name
```

📤 خروجی نمونه:

```
Please enter your name (type 'exit' to quit): Alice
Hello Alice! 😊
Please enter your name (type 'exit' to quit): Bob
Hello Bob! 😊
Please enter your name (type 'exit' to quit): exit
Exiting the program 👋
```

---

## 🧩 مثال ۴: استفاده از `continue` برای رد کردن یک مرحله

گاهی وقتا می‌خوای بعضی مراحل رد بشن ولی بقیه ادامه پیدا کنن.

```python
# Skip even numbers
n = 0

while n < 5:
    n += 1
    if n % 2 == 0:
        continue  # skip even numbers
    print(n)
```

📤 خروجی:

```
1
3
5
```

---

## ✏️ تمرین‌های کوچک برای دانشجو

🧮 **تمرین ۱:**
برنامه‌ای بنویس که از ۱ تا ۱۰ عددها رو چاپ کنه.

🔢 **تمرین ۲:**
برنامه‌ای بنویس که از ۱۰ تا ۱ شمارش معکوس انجام بده و بعد بنویسه “تمام شد! ✅”

💬 **تمرین ۳:**
برنامه‌ای بنویس که از کاربر نام بگیره تا وقتی “خروج” یا “exit” وارد کنه.

---

## 💡 نتیجه این صفحه

✅ یاد گرفتی که:

* ساختار حلقه‌ی `while` چیه
* چطور تکرار انجام می‌ده
* چطور با `break` ازش خارج می‌شی
* و با `continue` بعضی مراحل رو رد می‌کنی

---

فقط بنویس:

> «برو صفحه ۳ از فصل ۲»
