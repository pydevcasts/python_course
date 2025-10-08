

# 🐍 **فصل ۱: شروع ماجراجویی با پایتون**

## ✨ صفحه ۵: ساخت اولین پروژه واقعی — ماشین حساب ساده 🧮

تا اینجا یاد گرفتی چطور داده بگیری، چاپ کنی، با متغیرها و انواع داده‌ها کار کنی و ورودی رو تبدیل کنی.
حالا قراره همه‌ی این مهارت‌ها رو کنار هم بذاریم تا یه ماشین حساب ساده و دوست‌داشتنی بسازیم! 😍

---

## 💡 هدف این پروژه

می‌خوایم برنامه‌ای بسازیم که:

1. از کاربر دو عدد بگیره
2. بپرسه چه عملیاتی می‌خواد انجام بده (`+`, `-`, `*`, `/`)
3. نتیجه‌ی محاسبه رو نشون بده

یه ماشین حساب واقعی ولی با ظاهری پایتونی و شاد! 🎨

---

## 💻 مرحله ۱: طراحی ورودی‌ها

```python
# Simple Calculator Project 🧮
print("=== Welcome to Python Calculator ===")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation: +, -, *, /")
operation = input("Enter your choice: ")
```

✅ تا اینجا ما از کاربر دو عدد و یک عمل ریاضی گرفتیم.
الان فقط باید تصمیم بگیریم با اون داده‌ها چیکار کنیم 😎

---

## 🧠 مرحله ۲: تصمیم‌گیری با if و else

```python
# Performing the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result} ✅")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result} ✅")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} × {num2} = {result} ✅")

elif operation == '/':
    # check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} ÷ {num2} = {result} ✅")
    else:
        print("❌ Error: Division by zero is not allowed!")

else:
    print("⚠️ Invalid operation! Please try again.")
```

📤 مثال خروجی:

```
=== Welcome to Python Calculator ===
Enter the first number: 10
Enter the second number: 5
Choose an operation: +, -, *, /
Enter your choice: *
10.0 × 5.0 = 50.0 ✅
```

---

## 🎨 مرحله ۳: اضافه کردن جزئیات و زیبایی 😍

بیایم یه‌کم خوشگل‌ترش کنیم — مثلاً فاصله بین خطوط و شکلک اضافه کنیم 🎭

```python
print("✨ Result ✨")
print("========================")
print(f"{num1} {operation} {num2} = {result}")
print("========================")
print("Thanks for using Python Calculator 🐍💙")
```

📤 خروجی زیبا:

```
✨ Result ✨
========================
10.0 × 5.0 = 50.0
========================
Thanks for using Python Calculator 🐍💙
```

---

## 🧩 مرحله ۴: اضافه کردن چند ویژگی جدید

چون پایتون خیلی انعطاف‌پذیره، می‌تونی ویژگی‌های کوچیک ولی جذابی بهش اضافه کنی. مثلاً:

### 🎯 اجرای چندباره‌ی ماشین حساب (بدون بستن برنامه)

```python
# Repeat calculator until user quits
while True:
    print("\n=== Simple Python Calculator ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("❌ Cannot divide by zero!")
    else:
        print("⚠️ Invalid operation!")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("👋 Bye! Keep learning Python 🐍")
        break
```

📤 مثال خروجی:

```
=== Simple Python Calculator ===
Enter first number: 8
Enter second number: 2
Choose operation (+, -, *, /): /
Result: 4.0
Do you want to calculate again? (yes/no): no
👋 Bye! Keep learning Python 🐍
```

---

## 🧠 تمرین شماره ۳ — چالش هوشمندانه 🎯

برنامه‌ی ماشین حساب خودت رو طوری تغییر بده که:

1. عملگر **توان (^)** هم اضافه بشه.
2. اگر کاربر چیزی اشتباه وارد کرد، پیام خطا بده ولی **برنامه متوقف نشه**.
3. خروجی‌ها رو با ایموجی و ظاهر رنگی‌تر نشون بده (مثلاً ✨✅❌).

💬 نکته: برای محاسبه‌ی توان می‌تونی از `**` استفاده کنی:

```python
result = num1 ** num2
```

---

## 🧡 نکات طلایی این صفحه:

✅ یاد گرفتی چطور برنامه‌ای بنویسی که از کاربر ورودی بگیره
✅ با `if` و `elif` تصمیم‌گیری رو کنترل کردی
✅ خطای تقسیم بر صفر رو مدیریت کردی
✅ ظاهر برنامه‌ات رو جذاب‌تر و کاربرپسندتر کردی
✅ و اولین **پروژه‌ی واقعی پایتونت** رو ساختی! 🎉

---

> «برو فصل ۲ صفحه ۱»
