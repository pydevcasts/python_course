# صفحه ۱۶: دیکشنری‌ها (Dictionaries) - کار با کلید-مقدار، متدهای کاربردی، پیمایش

## هدف آموزشی
در این صفحه با ساختار داده دیکشنری در پایتون آشنا می‌شوید. یاد می‌گیرید چگونه از جفت‌های کلید-مقدار برای ذخیره و بازیابی داده‌ها استفاده کنید، با متدهای کاربردی دیکشنری کار کنید و تکنیک‌های مختلف پیمایش دیکشنری را بیاموزید.

## توضیح مفهومی

دیکشنری (Dictionary) یک ساختار داده **تغییرپذیر (Mutable)** و **نامرتب (Unordered)** در پایتون است که داده‌ها را به صورت جفت‌های **کلید-مقدار (Key-Value)** ذخیره می‌کند. هر کلید باید منحصر به فرد و **هش‌پذیر (Hashable)** باشد، در حالی که مقادیر می‌توانند از هر نوعی باشند.

### ویژگی‌های کلیدی دیکشنری

- دسترسی سریع به مقادیر از طریق کلیدها (با پیچیدگی زمانی O(1))
- کلیدها باید یکتا و غیرقابل تغییر (immutable) باشند
- مقادیر می‌توانند تکراری و از هر نوعی باشند
- از پایتون ۳.۷ به بعد، ترتیب درج عناصر حفظ می‌شود

### متدهای کاربردی دیکشنری

- `keys()`: بازگرداندن نمای تمام کلیدها
- `values()`: بازگرداندن نمای تمام مقادیر
- `items()`: بازگرداندن نمای تمام جفت‌های کلید-مقدار
- `get()`: دریافت مقدار با کلید مشخص (بدون خطا در صورت عدم وجود)
- `setdefault()`: تنظیم پیش‌فرض برای کلید در صورت عدم وجود
- `update()`: به‌روزرسانی دیکشنری با جفت‌های کلید-مقدار جدید
- `pop()`: حذف و بازگرداندن مقدار یک کلید
- `popitem()`: حذف و بازگرداندن آخرین جفت کلید-مقدار

## بخش کد عملی

### مثال ۱: کار با کلید-مقدار و متدهای کاربردی

```python
# Create a dictionary with student information
student_info = {
    "name": "Alice Johnson",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.85
}

# Access values using keys
print(f"Student name: {student_info['name']}")
print(f"Student age: {student_info['age']}")

# Use get() method (safe access - no error if key doesn't exist)
phone_number = student_info.get("phone", "Not provided")
print(f"Phone number: {phone_number}")

# Add a new key-value pair
student_info["email"] = "alice.johnson@university.edu"
print(f"After adding email: {student_info}")

# Update an existing value
student_info["gpa"] = 3.92
print(f"Updated GPA: {student_info['gpa']}")

# Use setdefault() to set default value
student_info.setdefault("graduation_year", 2024)
print(f"Graduation year: {student_info['graduation_year']}")

# Try setdefault on existing key (no change)
student_info.setdefault("age", 23)
print(f"Age after setdefault: {student_info['age']}")

# Get all keys
all_keys = student_info.keys()
print(f"All keys: {list(all_keys)}")

# Get all values
all_values = student_info.values()
print(f"All values: {list(all_values)}")

# Get all items (key-value pairs)
all_items = student_info.items()
print(f"All items: {list(all_items)}")

# Update dictionary with new data
additional_info = {"phone": "+1-555-0123", "city": "Boston"}
student_info.update(additional_info)
print(f"After update: {student_info}")

# Pop a specific key
removed_email = student_info.pop("email")
print(f"Removed email: {removed_email}")
print(f"After pop: {student_info}")

# Pop last item
last_item = student_info.popitem()
print(f"Popped item: {last_item}")
print(f"After popitem: {student_info}")
```

**تحلیل کد:**
در این مثال، ما یک دیکشنری برای ذخیره اطلاعات دانشجو ایجاد کردیم. متد `get()` برای دسترسی ایمن استفاده می‌شود (اگر کلید وجود نداشته باشد، خطا نمی‌دهد). متد `setdefault()` فقط در صورتی مقدار را تنظیم می‌کند که کلید از قبل وجود نداشته باشد. متدهای `keys()`، `values()` و `items()` نمای‌هایی از دیکشنری برمی‌گردانند که می‌توان آن‌ها را به لیست تبدیل کرد.

### مثال ۲: پیمایش دیکشنری و کاربردهای پیشرفته

```python
# Create a dictionary with product prices
product_prices = {
    "laptop": 999.99,
    "mouse": 29.99,
    "keyboard": 79.99,
    "monitor": 349.99,
    "headphones": 149.99
}

# Iterate through keys (default behavior)
print("Products:")
for product in product_prices:
    print(f"  - {product}")

# Iterate through keys explicitly
print("\nProducts (explicit keys):")
for product in product_prices.keys():
    print(f"  - {product}")

# Iterate through values
print("\nPrices:")
for price in product_prices.values():
    print(f"  - ${price:.2f}")

# Iterate through key-value pairs (recommended)
print("\nProduct Prices:")
for product, price in product_prices.items():
    print(f"  {product}: ${price:.2f}")

# Create dictionary from two lists using zip()
products = ["tablet", "charger", "usb_cable"]
prices = [499.99, 39.99, 19.99]
new_products_dict = dict(zip(products, prices))
print(f"\nNew products dictionary: {new_products_dict}")

# Dictionary comprehension - create discount prices
discounted_prices = {product: price * 0.8 for product, price in product_prices.items()}
print(f"\nDiscounted prices (20% off): {discounted_prices}")

# Filter dictionary using comprehension
expensive_products = {product: price for product, price in product_prices.items() if price > 100}
print(f"\nExpensive products (> $100): {expensive_products}")

# Nested dictionary
inventory = {
    "electronics": {
        "laptop": 50,
        "mouse": 200,
        "keyboard": 150
    },
    "accessories": {
        "headphones": 75,
        "usb_cable": 300
    }
}

# Access nested dictionary
print(f"\nLaptops in stock: {inventory['electronics']['laptop']}")

# Iterate through nested dictionary
print("\nInventory by category:")
for category, items in inventory.items():
    print(f"  {category}:")
    for item, quantity in items.items():
        print(f"    {item}: {quantity} units")
```

**تحلیل کد:**
این مثال تکنیک‌های مختلف پیمایش دیکشنری را نشان می‌دهد. پیمایش مستقیم دیکشنری معادل پیمایش کلیدهاست. برای دسترسی همزمان به کلید و مقدار، از متد `items()` استفاده می‌کنیم. همچنین با استفاده از **درک دیکشنری (Dictionary Comprehension)** می‌توان دیکشنری‌های جدید ایجاد یا فیلتر کرد. دیکشنری‌های تو در تو (Nested Dictionaries) برای ساختارهای داده پیچیده‌تر کاربرد دارند.

## تمرین (Exercise)

### تمرین ۱
یک دیکشنری بسازید که نمرات ۵ دانشجو را ذخیره کند (کلید: نام دانشجو، مقدار: نمره). سپس:
- میانگین نمرات را محاسبه کنید
- دانشجویانی که نمره بالای ۱۵ دارند را در یک دیکشنری جدید ذخیره کنید
- نام دانشجویی با بالاترین نمره را پیدا کنید

### تمرین ۲
تابعی بنویسید که یک رشته متن دریافت کند و تعداد تکرار هر کلمه را در یک دیکشنری برگرداند (کلید: کلمه، مقدار: تعداد تکرار).

---

<details>
<summary>پاسخ تشریحی تمرین‌ها</summary>

```python
# Exercise 1 Solution
# Create dictionary with student grades
student_grades = {
    "Ali": 18,
    "Sara": 16,
    "Reza": 14,
    "Maryam": 19,
    "Hassan": 12
}

# Calculate average grade
total_grade = sum(student_grades.values())
num_students = len(student_grades)
average_grade = total_grade / num_students
print(f"Average grade: {average_grade:.2f}")

# Filter students with grade above 15
high_achievers = {name: grade for name, grade in student_grades.items() if grade > 15}
print(f"High achievers (> 15): {high_achievers}")

# Find student with highest grade
top_student = max(student_grades, key=student_grades.get)
top_grade = student_grades[top_student]
print(f"Top student: {top_student} with grade {top_grade}")


# Exercise 2 Solution
def count_word_frequency(text):
    """Count frequency of each word in text"""
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove punctuation from words
    cleaned_words = []
    for word in words:
        cleaned_word = "".join(char for char in word if char.isalnum())
        if cleaned_word:
            cleaned_words.append(cleaned_word)
    
    # Count word frequencies
    word_frequency = {}
    for word in cleaned_words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    return word_frequency

# Test the function
sample_text = "Python is great Python is powerful Python is versatile"
frequency = count_word_frequency(sample_text)
print(f"Word frequency: {frequency}")
```

</details>

## جمع‌بندی

- ✅ دیکشنری‌ها ساختارهای داده **تغییرپذیر (Mutable)** بر پایه کلید-مقدار هستند
- ✅ کلیدها باید **هش‌پذیر (Hashable)** و یکتا باشند
- ✅ متد `get()` برای دسترسی ایمن بدون ایجاد خطا استفاده می‌شود
- ✅ متدهای `keys()`، `values()`، `items()` نمای‌هایی از دیکشنری برمی‌گردانند
- ✅ پیمایش مستقیم دیکشنری معادل پیمایش کلیدهاست
- ✅ برای پیمایش همزمان کلید و مقدار از `items()` استفاده کنید
- ✅ **درک دیکشنری (Dictionary Comprehension)** روشی مختصر برای ایجاد/فیلتر دیکشنری است
- ✅ دیکشنری‌ها از پایتون ۳.۷ ترتیب درج را حفظ می‌کنند
- ✅ دیکشنری‌های تو در تو برای ساختارهای داده پیچیده کاربرد دارند
