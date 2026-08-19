# صفحه ۱۵: لیست‌ها (Lists) - مرور پیشرفته، متدهای حیاتی، اسلایسینگ عمیق

## هدف آموزشی
در این صفحه با قابلیت‌های پیشرفته لیست‌ها در پایتون آشنا می‌شوید. یاد می‌گیرید چگونه از متدهای حیاتی لیست برای مدیریت داده‌ها استفاده کنید و با تکنیک‌های اسلایسینگ (Slicing) عمیق، برش‌های پیچیده‌ای از داده‌ها استخراج نمایید.

## توضیح مفهومی

لیست (List) یکی از پرکاربردترین ساختارهای داده در پایتون است که به شما امکان ذخیره مجموعه‌ای از آیتم‌ها را به ترتیب خاص می‌دهد. لیست‌ها **تغییرپذیر (Mutable)** هستند، یعنی می‌توانید پس از ایجاد، محتوای آن‌ها را تغییر دهید.

### متدهای حیاتی لیست

لیست‌ها متدهای متعددی دارند که برخی از مهم‌ترین آن‌ها عبارتند از:

- `append()`: افزودن یک عنصر به انتهای لیست
- `extend()`: افزودن چندین عنصر از یک iterable به انتهای لیست
- `insert()`: درج عنصر در موقعیت مشخص
- `remove()`: حذف اولین رخداد یک مقدار مشخص
- `pop()`: حذف و بازگرداندن عنصر در موقعیت مشخص (یا آخرین عنصر)
- `index()`: یافتن ایندکس اولین رخداد یک مقدار
- `count()`: شمارش تعداد رخداد یک مقدار
- `sort()`: مرتب‌سازی لیست در محل
- `reverse()`: معکوس کردن ترتیب عناصر در محل

### اسلایسینگ عمیق (Deep Slicing)

اسلایسینگ (Slicing) تکنیکی قدرتمند برای استخراج بخش‌هایی از لیست است. سینتکس کلی به صورت زیر است:

```python
list[start:stop:step]
```

- `start`: ایندکس شروع (شامل)
- `stop`: ایندکس پایان (شامل نیست)
- `step`: گام حرکت (پیش‌فرض ۱)

## بخش کد عملی

### مثال ۱: کار با متدهای حیاتی لیست

```python
# Initialize a list of programming languages
programming_languages = ["Python", "JavaScript", "Java"]

# Append a new language
programming_languages.append("C++")
print(f"After append: {programming_languages}")

# Extend with multiple languages
programming_languages.extend(["Ruby", "Go", "Rust"])
print(f"After extend: {programming_languages}")

# Insert at specific position
programming_languages.insert(2, "TypeScript")
print(f"After insert: {programming_languages}")

# Remove a specific element
programming_languages.remove("Java")
print(f"After remove: {programming_languages}")

# Pop an element (last by default)
removed_language = programming_languages.pop()
print(f"Popped language: {removed_language}")
print(f"After pop: {programming_languages}")

# Count occurrences
count_python = programming_languages.count("Python")
print(f"Count of Python: {count_python}")

# Sort the list
programming_languages.sort()
print(f"After sort: {programming_languages}")

# Reverse the list
programming_languages.reverse()
print(f"After reverse: {programming_languages}")
```

**تحلیل کد:**
در این مثال، ما یک لیست از زبان‌های برنامه‌نویسی ایجاد کردیم و سپس از متدهای مختلف برای تغییر و مدیریت آن استفاده نمودیم. توجه داشته باشید که متدهایی مانند `sort()` و `reverse()` لیست را در محل تغییر می‌دهند (in-place) و مقدار جدیدی برنمی‌گردانند.

### مثال ۲: اسلایسینگ عمیق و تکنیک‌های پیشرفته

```python
# Create a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic slicing - get elements from index 2 to 6
slice_1 = numbers[2:7]
print(f"numbers[2:7] = {slice_1}")

# Slice from beginning to index 5
slice_2 = numbers[:5]
print(f"numbers[:5] = {slice_2}")

# Slice from index 7 to end
slice_3 = numbers[7:]
print(f"numbers[7:] = {slice_3}")

# Slice with step - get every second element
slice_4 = numbers[::2]
print(f"numbers[::2] = {slice_4}")

# Slice with negative step - reverse the list
slice_5 = numbers[::-1]
print(f"numbers[::-1] = {slice_5}")

# Get last 3 elements using negative indexing
slice_6 = numbers[-3:]
print(f"numbers[-3:] = {slice_6}")

# Complex slice - start from index 8, go backwards by 2, stop before index 2
slice_7 = numbers[8:2:-2]
print(f"numbers[8:2:-2] = {slice_7}")

# Copy a list using slicing
numbers_copy = numbers[:]
print(f"Copy of numbers: {numbers_copy}")

# Modify a slice (replace elements)
numbers[2:5] = [20, 30, 40]
print(f"After modifying slice: {numbers}")
```

**تحلیل کد:**
این مثال قدرت اسلایسینگ در پایتون را نشان می‌دهد. شما می‌توانید با استفاده از گام‌های منفی، لیست را معکوس کنید، یا با ترکیب ایندکس‌های مثبت و منفی، برش‌های پیچیده‌ای ایجاد نمایید. همچنین می‌توانید با اختصاص دادن یک لیست جدید به یک اسلایس، عناصر آن بخش را جایگزین کنید.

## تمرین (Exercise)

### تمرین ۱
یک لیست از اعداد صحیح از ۱ تا ۲۰ ایجاد کنید. سپس:
- تمام اعداد زوج را با استفاده از اسلایسینگ استخراج کنید
- سه عدد آخر لیست را معکوس کرده و در جای خود قرار دهید
- لیست نهایی را مرتب نزولی کنید

### تمرین ۲
تابعی بنویسید که یک لیست دریافت کند و بدون استفاده از متد `reverse()`، لیست را معکوس نماید (با استفاده از اسلایسینگ).

---

<details>
<summary>پاسخ تشریحی تمرین‌ها</summary>

```python
# Exercise 1 Solution
# Create list from 1 to 20
numbers_list = list(range(1, 21))
print(f"Original list: {numbers_list}")

# Extract even numbers using slicing
even_numbers = numbers_list[1::2]
print(f"Even numbers: {even_numbers}")

# Reverse last 3 elements and replace them
numbers_list[-3:] = numbers_list[-3:][::-1]
print(f"After reversing last 3: {numbers_list}")

# Sort in descending order
numbers_list.sort(reverse=True)
print(f"Final sorted list: {numbers_list}")


# Exercise 2 Solution
def reverse_list(input_list):
    """Reverse a list using slicing without using reverse() method"""
    return input_list[::-1]

# Test the function
test_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(test_list)
print(f"Original: {test_list}")
print(f"Reversed: {reversed_list}")
```

</details>

## جمع‌بندی

- ✅ لیست‌ها ساختارهای داده **تغییرپذیر (Mutable)** و有序 (Ordered) هستند
- ✅ متدهای `append()`، `extend()`، `insert()` برای افزودن عناصر استفاده می‌شوند
- ✅ متدهای `remove()`، `pop()` برای حذف عناصر کاربرد دارند
- ✅ متدهای `sort()` و `reverse()` لیست را در محل تغییر می‌دهند
- ✅ اسلایسینگ با سینتکس `[start:stop:step]` امکان استخراج بخش‌های مختلف لیست را می‌دهد
- ✅ گام منفی در اسلایسینگ باعث پیمایش معکوس می‌شود
- ✅ می‌توان با اسلایسینگ `[:]` یک کپی از لیست ایجاد کرد
- ✅ اسلایس‌ها قابل تخصیص مجدد هستند و می‌توان عناصر آن‌ها را جایگزین کرد
