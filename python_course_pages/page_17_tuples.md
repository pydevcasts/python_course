# صفحه ۱۷: تاپل‌ها (Tuples) - تعریف، تفاوت با لیست، کاربردها در برگشت چند مقداری توابع

## هدف آموزشی
در این صفحه با ساختار داده تاپل آشنا می‌شوید. یاد می‌گیرید چگونه تاپل‌ها را تعریف کنید، تفاوت‌های کلیدی آن‌ها با لیست‌ها را درک نمایید و از تاپل‌ها برای برگشت چندین مقدار از توابع استفاده کنید.

## توضیح مفهومی

تاپل (Tuple) یک ساختار داده **تغییرناپذیر (Immutable)** و **مرتب (Ordered)** در پایتون است که شبیه به لیست عمل می‌کند، با این تفاوت مهم که پس از ایجاد نمی‌توان آن را تغییر داد. این ویژگی تاپل‌ها را برای داده‌هایی که نباید تغییر کنند، ایده‌آل می‌سازد.

### چرا از تاپل استفاده کنیم؟

1. **امنیت داده**: چون تاپل تغییرناپذیر است، مطمئن هستید که داده‌ها تصادفی تغییر نمی‌کنند
2. **کارایی**: تاپل‌ها سریع‌تر از لیست‌ها هستند و حافظه کمتری مصرف می‌کنند
3. **قابلیت هش‌پذیری**: تاپل‌ها (اگر عناصرشان هش‌پذیر باشند) می‌توانند به عنوان کلید دیکشنری استفاده شوند
4. **معنای کد**: استفاده از تاپل نشان می‌دهد که داده‌ها ثابت هستند

### تعریف تاپل

- تاپل با پرانتز `()` تعریف می‌شود
- عناصر با کاما از هم جدا می‌شوند
- برای تاپل تک‌عضوی، حتماً باید بعد از عنصر کاما بگذارید: `(value,)`
- تاپل خالی: `()`

## بخش کد عملی

### مثال ۱: تعریف تاپل و تفاوت با لیست

```python
# Define tuples in different ways
coordinates = (10, 20, 30)
colors = "red", "green", "blue"  # Parentheses are optional
single_element = (42,)  # Note the comma - this is a tuple
empty_tuple = ()

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Single element tuple: {single_element}")
print(f"Empty tuple: {empty_tuple}")

# Access tuple elements (same as lists)
print(f"\nFirst coordinate: {coordinates[0]}")
print(f"Last color: {colors[-1]}")

# Tuple slicing (same as lists)
print(f"First two coordinates: {coordinates[0:2]}")
print(f"All colors reversed: {colors[::-1]}")

# Try to modify a tuple (this will cause an error)
try:
    coordinates[0] = 100
    print("Modification succeeded")
except TypeError as e:
    print(f"\nError when modifying tuple: {e}")

# Compare with list (mutable)
coordinates_list = [10, 20, 30]
coordinates_list[0] = 100  # This works fine
print(f"Modified list: {coordinates_list}")

# Tuple unpacking
x, y, z = coordinates
print(f"\nUnpacked values: x={x}, y={y}, z={z}")

# Swap variables using tuple unpacking
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Elegant swap using tuples
print(f"After swap: a={a}, b={b}")

# Tuple methods
sample_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = sample_tuple.count(2)
index_of_4 = sample_tuple.index(4)

print(f"\nCount of 2: {count_of_2}")
print(f"Index of 4: {index_of_4}")

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"\nNested tuple: {nested}")
print(f"Element at [1][0]: {nested[1][0]}")

# Tuple with mixed data types
mixed_tuple = ("Alice", 25, 3.85, ["Math", "Physics"])
print(f"\nMixed tuple: {mixed_tuple}")
# Note: The list inside tuple can still be modified
mixed_tuple[3].append("Chemistry")
print(f"After modifying inner list: {mixed_tuple}")
```

**تحلیل کد:**
در این مثال، روش‌های مختلف تعریف تاپل را مشاهده می‌کنید. نکته مهم این است که تاپل تک‌عضوی نیاز به کاما دارد. تاپل‌ها مانند لیست‌ها قابل ایندکس‌گذاری و اسلایس هستند، اما نمی‌توان عناصر آن‌ها را تغییر داد. همچنین می‌توانید از تاپل برای جابجایی مقادیر متغیرها بدون متغیر موقت استفاده کنید. توجه کنید که اگر تاپل حاوی اشیاء تغییرپذیر (مثل لیست) باشد، آن اشیاء همچنان قابل تغییر هستند.

### مثال ۲: برگشت چند مقداری از توابع با تاپل

```python
# Function returning multiple values using tuple
def calculate_statistics(numbers):
    """Calculate and return multiple statistics"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    minimum = min(numbers)
    maximum = max(numbers)
    
    # Return multiple values as a tuple
    return total, count, average, minimum, maximum

# Test the function
data = [15, 25, 35, 45, 55]
result = calculate_statistics(data)
print(f"Full result tuple: {result}")
print(f"Type of result: {type(result)}")

# Unpack the returned tuple
total, count, avg, min_val, max_val = calculate_statistics(data)
print(f"\nUnpacked results:")
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {avg:.2f}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")

# Ignore some values using underscore
total_only, _, _, _, _ = calculate_statistics(data)
print(f"\nOnly total: {total_only}")

# Function returning student info as tuple
def get_student_info(student_id):
    """Return student information as tuple"""
    # Simulated database lookup
    students_db = {
        101: ("Ali Rezaei", "Computer Science", 3.75),
        102: ("Sara Mohammadi", "Mathematics", 3.92),
        103: ("Hassan Ahmadi", "Physics", 3.65)
    }
    return students_db.get(student_id, ("Unknown", "N/A", 0.0))

# Get and unpack student info
student_id = 102
name, major, gpa = get_student_info(student_id)
print(f"\nStudent {student_id}:")
print(f"Name: {name}")
print(f"Major: {major}")
print(f"GPA: {gpa}")

# Using tuple as dictionary key (because it's hashable)
location_coordinates = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (48.8566, 2.3522): "Paris"
}

ny_coordinates = (40.7128, -74.0060)
print(f"\nCity at {ny_coordinates}: {location_coordinates[ny_coordinates]}")

# Iterate through tuple of tuples
employee_records = (
    ("E001", "John Doe", "Engineering"),
    ("E002", "Jane Smith", "Marketing"),
    ("E003", "Bob Johnson", "Sales")
)

print("\nEmployee Records:")
for emp_id, name, department in employee_records:
    print(f"  {emp_id}: {name} - {department}")
```

**تحلیل کد:**
این مثال نشان می‌دهد که چگونه توابع می‌توانند چندین مقدار را به صورت تاپل برگردانند. وقتی تابعی چند مقدار را برمی‌گرداند، در واقع یک تاپل برمی‌گرداند. شما می‌توانید این تاپل را در یک متغیر ذخیره کنید یا مستقیماً آن را باز کنید (unpack). همچنین می‌توانید با استفاده از `_` برخی مقادیر را نادیده بگیرید. یکی از کاربردهای مهم تاپل، استفاده به عنوان کلید دیکشنری است، زیرا تاپل‌ها هش‌پذیر هستند (به شرطی که عناصرشان نیز هش‌پذیر باشند).

## تمرین (Exercise)

### تمرین ۱
تابعی بنویسید که دو عدد دریافت کند و یک تاپل شامل موارد زیر برگرداند:
- جمع دو عدد
- تفاضل دو عدد
- ضرب دو عدد
- تقسیم دو عدد

سپس نتایج را از تاپل استخراج کرده و نمایش دهید.

### تمرین ۲
یک لیست از تاپل‌ها ایجاد کنید که هر تاپل شامل (نام محصول، قیمت، تعداد) باشد. سپس:
- کل ارزش انبار (مجموع قیمت × تعداد برای همه محصولات) را محاسبه کنید
- گران‌ترین محصول را پیدا کنید
- محصولاتی که قیمت بالای ۱۰۰ دارند را فیلتر کنید

---

<details>
<summary>پاسخ تشریحی تمرین‌ها</summary>

```python
# Exercise 1 Solution
def calculate_operations(a, b):
    """Perform basic operations and return results as tuple"""
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else float('inf')
    
    return addition, subtraction, multiplication, division

# Test the function
num1 = 20
num2 = 4
result_tuple = calculate_operations(num1, num2)

print(f"Numbers: {num1} and {num2}")
print(f"Results tuple: {result_tuple}")

# Unpack and display
add, sub, mul, div = calculate_operations(num1, num2)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div:.2f}")


# Exercise 2 Solution
# Create list of tuples (product_name, price, quantity)
inventory = [
    ("Laptop", 999.99, 10),
    ("Mouse", 29.99, 50),
    ("Keyboard", 79.99, 30),
    ("Monitor", 349.99, 15),
    ("Headphones", 149.99, 25),
    ("USB Cable", 9.99, 100)
]

# Calculate total inventory value
total_value = sum(price * quantity for _, price, quantity in inventory)
print(f"\nTotal inventory value: ${total_value:.2f}")

# Find most expensive product
most_expensive = max(inventory, key=lambda item: item[1])
print(f"Most expensive product: {most_expensive[0]} (${most_expensive[1]:.2f})")

# Filter products with price > 100
expensive_products = [(name, price, qty) for name, price, qty in inventory if price > 100]
print(f"\nProducts with price > $100:")
for product in expensive_products:
    print(f"  - {product[0]}: ${product[1]:.2f} ({product[2]} units)")
```

</details>

## جمع‌بندی

- ✅ تاپل‌ها ساختارهای داده **تغییرناپذیر (Immutable)** و مرتب هستند
- ✅ تاپل با پرانتز `()` یا حتی بدون پرانتز (با کاما) تعریف می‌شود
- ✅ تاپل تک‌عضوری نیاز به کاما دارد: `(value,)`
- ✅ تاپل‌ها سریع‌تر از لیست‌ها هستند و حافظه کمتری مصرف می‌کنند
- ✅ تاپل‌ها **هش‌پذیر (Hashable)** هستند (اگر عناصرشان هش‌پذیر باشند)
- ✅ می‌توان تاپل را به عنوان کلید دیکشنری استفاده کرد
- ✅ توابع با برگرداندن تاپل، امکان برگشت چندین مقدار را فراهم می‌کنند
- ✅ **باز کردن تاپل (Tuple Unpacking)** روشی زیبا برای تخصیص چند متغیر است
- ✅ تاپل‌ها فقط دو متد دارند: `count()` و `index()`
- ✅ اگر تاپل حاوی اشیاء تغییرپذیر باشد، آن اشیاء همچنان قابل تغییر هستند
