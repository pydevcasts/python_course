👇

# 🐍 **فصل ۱: شروع ماجراجویی با پایتون**

## ✨ صفحه ۲: اولین برنامه واقعی — شناخت ساختار کدها در پایتون 💡

خب حالا که پایتون و VS Code رو نصب کردی و اولین `Hello, World!` رو نوشتی، وقتشه با ساختار واقعی برنامه‌نویسی پایتون آشنا بشیم 😎
قراره یاد بگیری چطور پایتون فکر می‌کنه، چطور کدها رو اجرا می‌کنه، و چطور می‌تونی خودت باهاش صحبت کنی 🧠

---

### 🚀 شروع ماجرا: اجرای خط‌به‌خط کد

پایتون کدها رو **از بالا به پایین** و **خط‌به‌خط** اجرا می‌کنه.
یعنی هر خطی که بنویسی، از بالا شروع می‌کنه تا برسه به آخر فایل.

👀 مثال ساده:

```python
print("Line 1 ✅")
print("Line 2 ✅")
print("Line 3 ✅")
```

📤 خروجی:

```
Line 1 ✅
Line 2 ✅
Line 3 ✅
```

اگر وسط راه خطایی وجود داشته باشه، پایتون بلافاصله متوقف میشه و اون خطا رو بهت نشون میده.

---

## 🧩 چند برنامه ساده برای آشنایی با متغیرها در پایتون

### 💻 مثال ۱: تعریف ساده‌ی متغیرها

```python
# Simple variable assignment
name = "Siamak"
age = 25
language = "Python"

print("My name is", name)
print("I'm", age, "years old.")
print("I love", language, "🐍")
```

📤 خروجی:

```
My name is Siamak
I'm 25 years old.
I love Python 🐍
```

---

### 🎯 نکته مهم:

در پایتون نیازی نیست نوع داده (مثل int یا string) رو موقع تعریف مشخص کنی.
پایتون خودش به صورت **هوشمندانه** نوع داده رو تشخیص می‌ده 🤓

---

### 💻 مثال ۲: تغییر مقدار متغیر در طول برنامه

```python
# Variables can be changed easily
counter = 1
print("Counter:", counter)

counter = counter + 1
print("Counter after adding 1:", counter)

counter += 5  # shorthand for counter = counter + 5
print("Counter after adding 5:", counter)
```

📤 خروجی:

```
Counter: 1
Counter after adding 1: 2
Counter after adding 5: 7
```

---

### 💻 مثال ۳: کار با رشته‌ها (String variables)

```python
# String operations
first_name = "Siamak"
last_name = "Abbasnejad"

full_name = first_name + " " + last_name
print("Full name:", full_name)

# String repetition
laugh = "Ha " * 3
print(laugh, "😂")
```

📤 خروجی:

```
Full name: Siamak Abbasnejad
Ha Ha Ha  😂
```

---

### 💻 مثال ۴: ترکیب متغیرهای مختلف در جمله

```python
# Mixing variables and strings
name = "Sara"
age = 19
language = "Python"

print(f"Hi {name}! You're {age} years old and learning {language}! 🚀")
```

📤 خروجی:

```
Hi Sara! You're 19 years old and learning Python! 🚀
```

✅ نکته: حرف `f` قبل از رشته یعنی **f-string** — یکی از راحت‌ترین روش‌ها برای قالب‌بندی متن‌ها در پایتونه.

---

این فقط پیش‌نمایش بود برای آماده‌سازی ذهن قبل از رفتن به صفحه‌ی بعد.
در صفحه‌ی سوم، مفصل‌تر توضیح می‌دیم:

* انواع داده‌ها (int, float, str, bool)
* تفاوت بین نوع داده‌ها
* چطور بفهمیم نوع داده‌ی یه متغیر چیه
* تمرین عملی ترکیب داده‌ها

