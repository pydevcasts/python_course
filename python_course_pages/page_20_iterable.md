# صفحه ۲۰: ایتریبل بودن (Iterable) - پروتکل تکرار، تفاوت iterable و iterator، حلقه‌های for زیر کاپوت

## هدف آموزشی
در این صفحه با مفهوم ایتریبل (Iterable) و ایتریتور (Iterator) در پایتون آشنا می‌شوید. یاد می‌گیرید پروتکل تکرار چگونه کار می‌کند و حلقه‌های `for` در پشت صحنه چه مراحلی را انجام می‌دهند.

## توضیح مفهومی

**ایتریبل (Iterable)** هر شیئی در پایتون است که بتوانیم روی آن تکرار (iterate) کنیم. به عبارت دیگر، ایتریبل شیئی است که می‌تواند یک **ایتریتور (Iterator)** برگرداند. مثال‌ها شامل لیست‌ها، تاپل‌ها، دیکشنری‌ها، ست‌ها، رشته‌ها و رنج‌ها هستند.

**ایتریتور (Iterator)** شیئی است که تکرار را مدیریت می‌کند و وضعیت فعلی تکرار را نگه می‌دارد. ایتریتور دو متد دارد:
- `__iter__()`: خود ایتریتور را برمی‌گرداند (برای سازگاری با پروتکل iterable)
- `__next__()`: عنصر بعدی را برمی‌گرداند یا اگر تکرار تمام شده باشد، خطای `StopIteration` می‌دهد

### تفاوت کلیدی

| ویژگی | Iterable | Iterator |
|-------|----------|----------|
| تعریف | شیئی که می‌توان روی آن تکرار کرد | شیئی که تکرار را مدیریت می‌کند |
| متدها | `__iter__()` | `__iter__()`, `__next__()` |
| وضعیت | وضعیت تکرار را نگه نمی‌دارد | وضعیت تکرار را نگه می‌دارد |
| مثال | list, tuple, dict, str | نتیجه `iter(list)` |
| چندبار مصرف | ✅ بله | ❌ خیر (یکبار مصرف) |

### پروتکل تکرار در پایتون

وقتی از حلقه `for` استفاده می‌کنید، پایتون در پشت صحنه مراحل زیر را انجام می‌دهد:

1. فراخوانی `iter()` روی ایتریبل برای دریافت ایتریتور
2. فراخوانی مکرر `next()` روی ایتریتور
3. هنگام رسیدن به پایان، دریافت خطای `StopIteration` و خروج از حلقه

## بخش کد عملی

### مثال ۱: بررسی Iterable و Iterator

```python
# ============ CHECKING ITERABLE AND ITERATOR ============

print("=== Checking Iterable and Iterator ===\n")

# Create an iterable (list)
my_list = [1, 2, 3, 4, 5]
print(f"My list: {my_list}")

# Check if object is iterable
from collections.abc import Iterable, Iterator

print(f"Is list iterable? {isinstance(my_list, Iterable)}")
print(f"Is list an iterator? {isinstance(my_list, Iterator)}")

# Get an iterator from the iterable
my_iterator = iter(my_list)
print(f"\nIterator from list: {my_iterator}")
print(f"Is iterator iterable? {isinstance(my_iterator, Iterable)}")
print(f"Is iterator an iterator? {isinstance(my_iterator, Iterator)}")

# Manually iterate using next()
print("\nManual iteration with next():")
print(f"First element: {next(my_iterator)}")
print(f"Second element: {next(my_iterator)}")
print(f"Third element: {next(my_iterator)}")

# Continue until exhaustion
print(f"Fourth element: {next(my_iterator)}")
print(f"Fifth element: {next(my_iterator)}")

# Try to get next element after exhaustion
try:
    print(f"Sixth element: {next(my_iterator)}")
except StopIteration:
    print("StopIteration raised - No more elements!")

print("\nNote: This iterator is now exhausted!")


# ============ STRING AS ITERABLE ============

print("\n=== String as Iterable ===\n")

text = "Python"
print(f"Text: '{text}'")
print(f"Is string iterable? {isinstance(text, Iterable)}")

text_iterator = iter(text)
print(f"First char: {next(text_iterator)}")
print(f"Second char: {next(text_iterator)}")

# Iterate through remaining characters
print("Remaining characters:")
for char in text_iterator:
    print(f"  '{char}'")
```

**تحلیل کد:**
این مثال نشان می‌دهد که چگونه می‌توان بررسی کرد یک شیء iterable یا iterator است. تابع `iter()` یک iterator از iterable می‌سازد و تابع `next()` عناصر را یکی یکی برمی‌گرداند. وقتی iterator تمام می‌شود، خطای `StopIteration` ایجاد می‌شود. توجه کنید که iterator یکبار مصرف است و پس از اتمام باید iterator جدیدی ساخت.

### مثال ۲: حلقه for زیر کاپوت

```python
# ============ HOW FOR LOOP WORKS INTERNALLY ============

print("=== How For Loop Works Internally ===\n")

# Normal for loop
numbers = [10, 20, 30, 40, 50]
print("Using for loop:")
for num in numbers:
    print(f"  {num}")

# Equivalent while loop showing what happens internally
print("\nEquivalent internal process:")
iterator = iter(numbers)  # Step 1: Get iterator
while True:
    try:
        item = next(iterator)  # Step 2: Get next element
        print(f"  {item}")
    except StopIteration:  # Step 3: Handle end of iteration
        print("  StopIteration caught - loop ends")
        break


# ============ CUSTOM ITERABLE CLASS ============

print("\n=== Custom Iterable Class ===\n")

class CountDown:
    """A custom iterable class"""
    
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        """Return an iterator"""
        return CountDownIterator(self.start)


class CountDownIterator:
    """A custom iterator class"""
    
    def __init__(self, current):
        self.current = current
    
    def __iter__(self):
        """Return self as iterator"""
        return self
    
    def __next__(self):
        """Return next value or raise StopIteration"""
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# Use the custom iterable
countdown = CountDown(5)
print(f"Is CountDown iterable? {isinstance(countdown, Iterable)}")

print("\nIterating through CountDown:")
for number in countdown:
    print(f"  {number}")

print("\nIterating again (creates new iterator):")
for number in countdown:
    print(f"  {number}")


# ============ CUSTOM ITERATOR WITH STATE ============

print("\n=== Custom Iterator with State ===\n")

class SquareIterator:
    """Iterator that returns squares of numbers"""
    
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


# Use the iterator
squares = SquareIterator(5)
print("Squares from 1 to 5:")
for square in squares:
    print(f"  {square}")

# Try to iterate again (exhausted!)
print("\nTrying to iterate again:")
for square in squares:
    print(f"  {square}")
print("Nothing printed - iterator was exhausted!")
```

**تحلیل کد:**
این مثال نشان می‌دهد که حلقه `for` در واقع یک حلقه `while` با مدیریت خطای `StopIteration` است. همچنین کلاس‌های custom iterable و iterator را مشاهده می‌کنید. نکته مهم این است که iterable باید متد `__iter__()` داشته باشد که یک iterator برمی‌گرداند، و iterator باید هم `__iter__()` و هم `__next__()` داشته باشد. iterator یکبار مصرف است و پس از اتمام باید جدید ساخته شود.

### مثال ۳: کاربردهای پیشرفته و Generator

```python
# ============ GENERATOR EXPRESSIONS ============

print("=== Generator Expressions ===\n")

# List comprehension (creates entire list in memory)
list_comp = [x ** 2 for x in range(5)]
print(f"List comprehension: {list_comp}")
print(f"Type: {type(list_comp)}")

# Generator expression (creates iterator, lazy evaluation)
gen_expr = (x ** 2 for x in range(5))
print(f"\nGenerator expression: {gen_expr}")
print(f"Type: {type(gen_expr)}")
print(f"Is iterator? {isinstance(gen_expr, Iterator)}")

print("\nGenerator values (lazy evaluation):")
for value in gen_expr:
    print(f"  {value}")


# ============ BUILT-IN ITERATORS ============

print("\n=== Built-in Iterators ===\n")

# Dictionary iteration
student_grades = {"Alice": 90, "Bob": 85, "Charlie": 92}

print("Dictionary keys:")
for key in student_grades:
    print(f"  {key}")

print("\nDictionary values:")
for value in student_grades.values():
    print(f"  {value}")

print("\nDictionary items:")
for key, value in student_grades.items():
    print(f"  {key}: {value}")

# Range is iterable but not a list
print("\nRange object:")
range_obj = range(3, 10, 2)
print(f"Range: {range_obj}")
print(f"Type: {type(range_obj)}")
print(f"Is iterable? {isinstance(range_obj, Iterable)}")

print("Range values:")
for num in range_obj:
    print(f"  {num}")


# ============ MULTIPLE ITERATORS FROM SAME ITERABLE ============

print("\n=== Multiple Iterators from Same Iterable ===\n")

colors = ["red", "green", "blue"]

# Create multiple iterators from same list
iter1 = iter(colors)
iter2 = iter(colors)

print(f"First iterator: {next(iter1)}")
print(f"Second iterator: {next(iter2)}")
print(f"First iterator again: {next(iter1)}")
print(f"Second iterator again: {next(iter2)}")

print("\nBoth iterators maintain independent state!")
print("This is why you can iterate over a list multiple times.")
```

**تحلیل کد:**
Generator Expressionها روشی مختصر برای ایجاد iterator هستند. برخلاف List Comprehension که کل لیست را در حافظه می‌سازد، Generator Expressionها مقدارها را به صورت تنبلانه (lazy) تولید می‌کنند. دیکشنری‌ها و rangeها نیز iterable هستند. نکته مهم این است که از یک iterable می‌توان چندین iterator مستقل ساخت که هر کدام وضعیت خود را دارند.

## تمرین (Exercise)

### تمرین ۱
یک کلاس بنویسید که یک iterable از اعداد فیبوناچی تا n عدد را تولید کند. سپس از آن در یک حلقه `for` استفاده کنید.

### تمرین ۲
تابعی بنویسید که یک iterable دریافت کند و بدون استفاده از حلقه `for`، تعداد عناصر آن را بشمارد (با استفاده از `iter()` و `next()`).

---

<details>
<summary>پاسخ تشریحی تمرین‌ها</summary>

```python
# Exercise 1 Solution
class FibonacciIterable:
    """Iterable that generates Fibonacci numbers"""
    
    def __init__(self, count):
        self.count = count
    
    def __iter__(self):
        return FibonacciIterator(self.count)


class FibonacciIterator:
    """Iterator for Fibonacci sequence"""
    
    def __init__(self, count):
        self.count = count
        self.current = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.count:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current += 1
        return result


# Test the Fibonacci iterable
print("First 10 Fibonacci numbers:")
fib = FibonacciIterable(10)
for num in fib:
    print(f"  {num}")


# Exercise 2 Solution
def count_iterable_elements(iterable):
    """Count elements without using for loop"""
    iterator = iter(iterable)
    count = 0
    
    while True:
        try:
            next(iterator)
            count += 1
        except StopIteration:
            break
    
    return count

# Test the function
test_list = [10, 20, 30, 40, 50]
test_string = "Hello"
test_tuple = (1, 2, 3, 4, 5, 6, 7)

print(f"List count: {count_iterable_elements(test_list)}")
print(f"String count: {count_iterable_elements(test_string)}")
print(f"Tuple count: {count_iterable_elements(test_tuple)}")
```

</details>

## جمع‌بندی

- ✅ **Iterable**: شیئی که متد `__iter__()` دارد و iterator برمی‌گرداند
- ✅ **Iterator**: شیئی با متدهای `__iter__()` و `__next__()`
- ✅ همه iteratorها iterable هستند، اما عکس آن صادق نیست
- ✅ iteratorها وضعیت تکرار را نگه می‌دارند و یکبار مصرف هستند
- ✅ حلقه `for` در پشت صحنه از `iter()` و `next()` با مدیریت `StopIteration` استفاده می‌کند
- ✅ از یک iterable می‌توان چندین iterator مستقل ساخت
- ✅ **Generator Expression** `(x for x in iterable)` iterator می‌سازد
- ✅ **List Comprehension** `[x for x in iterable]` لیست می‌سازد
- ✅ Generatorها محاسبه را به تعویق می‌اندازند (lazy evaluation)
- ✅ `range()` یک iterable است نه لیست
