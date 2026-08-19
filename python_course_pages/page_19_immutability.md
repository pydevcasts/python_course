# صفحه ۱۹: تغییرناپذیری (Immutability) - مفهوم عمیق، تأثیر روی حافظه، تفاوت اشیاء قابل و غیرقابل تغییر

## هدف آموزشی
در این صفحه با مفهوم عمیق تغییرناپذیری (Immutability) در پایتون آشنا می‌شوید. یاد می‌گیرید چگونه اشیاء تغییرپذیر و تغییرناپذیر در حافظه مدیریت می‌شوند و این تفاوت‌ها چه تأثیری روی عملکرد و طراحی کد شما دارند.

## توضیح مفهومی

**تغییرناپذیری (Immutability)** یکی از مفاهیم بنیادی در پایتون است که تعیین می‌کند آیا یک شیء پس از ایجاد قابل تغییر است یا خیر. درک این مفهوم برای نوشتن کد کارآمد و بدون باگ ضروری است.

### انواع اشیاء از نظر تغییرپذیری

**اشیاء تغییرناپذیر (Immutable Objects):**
- اعداد (int, float, complex)
- رشته‌ها (str)
- تاپل‌ها (tuple)
- فروزن‌ست‌ها (frozenset)

**اشیاء تغییرپذیر (Mutable Objects):**
- لیست‌ها (list)
- دیکشنری‌ها (dict)
- ست‌ها (set)
- اشیاء تعریف شده توسط کاربر (به صورت پیش‌فرض)

### چرا تغییرناپذیری مهم است؟

1. **امنیت در توابع**: وقتی یک شیء تغییرناپذیر را به تابع پاس می‌دهید، مطمئن هستید که تغییر نمی‌کند
2. **قابلیت هش‌پذیری**: فقط اشیاء تغییرناپذیر می‌توانند به عنوان کلید دیکشنری استفاده شوند
3. **اشتراک‌گذاری ایمن**: اشیاء تغییرناپذیر را می‌توان بین بخش‌های مختلف برنامه به اشتراک گذاشت
4. **بهینه‌سازی حافظه**: پایتون می‌تواند اشیاء تغییرناپذیر یکسان را در حافظه به اشتراک بگذارد

## بخش کد عملی

### مثال ۱: رفتار اشیاء تغییرپذیر و تغییرناپذیر

```python
# ============ IMMUTABLE OBJECTS ============

print("=== Immutable Objects ===\n")

# Integer example
x = 10
print(f"Initial x: {x}, id(x): {id(x)}")

x = x + 5  # Creates a new object, doesn't modify existing one
print(f"After x = x + 5: {x}, id(x): {id(x)}")
print("Note: A new integer object was created\n")

# String example
text = "Hello"
print(f"Initial text: '{text}', id(text): {id(text)}")

text = text + " World"  # Creates a new string object
print(f"After concatenation: '{text}', id(text): {id(text)}")
print("Note: A new string object was created\n")

# Tuple example
my_tuple = (1, 2, 3)
print(f"Initial tuple: {my_tuple}, id(my_tuple): {id(my_tuple)}")

# Try to modify tuple element (will fail)
try:
    my_tuple[0] = 999
except TypeError as e:
    print(f"Error when modifying tuple: {e}")
    print("Note: Cannot modify tuple elements\n")


# ============ MUTABLE OBJECTS ============

print("\n=== Mutable Objects ===\n")

# List example
my_list = [1, 2, 3]
print(f"Initial list: {my_list}, id(my_list): {id(my_list)}")

my_list.append(4)  # Modifies the same object in place
print(f"After append: {my_list}, id(my_list): {id(my_list)}")
print("Note: Same object, modified in place\n")

# Dictionary example
my_dict = {"name": "Alice", "age": 25}
print(f"Initial dict: {my_dict}, id(my_dict): {id(my_dict)}")

my_dict["city"] = "Boston"  # Modifies the same object
print(f"After adding key: {my_dict}, id(my_dict): {id(my_dict)}")
print("Note: Same object, modified in place\n")

# Important: Reassignment vs Modification
list_original = [1, 2, 3]
list_reference = list_original

print(f"\nOriginal list id: {id(list_original)}")
print(f"Reference list id: {id(list_reference)}")
print(f"Same object? {list_original is list_reference}")

# Modify through reference
list_reference.append(4)
print(f"\nAfter modifying through reference:")
print(f"Original: {list_original}")
print(f"Reference: {list_reference}")
print("Both changed because they reference the same object!")

# Now with immutable (string)
string_original = "Hello"
string_reference = string_original

print(f"\nOriginal string id: {id(string_original)}")
print(f"Reference string id: {id(string_reference)}")

# "Modify" through reference (actually creates new object)
string_reference = string_reference + " World"
print(f"\nAfter 'modification':")
print(f"Original: '{string_original}'")
print(f"Reference: '{string_reference}'")
print("Original unchanged because strings are immutable!")
```

**تحلیل کد:**
این مثال تفاوت بنیادی بین اشیاء تغییرپذیر و تغییرناپذیر را نشان می‌دهد. وقتی یک شیء تغییرناپذیر را "تغییر" می‌دهید، در واقع یک شیء جدید در حافظه ایجاد می‌شود و متغیر به آن اشاره می‌کند. اما اشیاء تغییرپذیر در محل خود تغییر می‌کنند و شناسه (id) آن‌ها ثابت می‌ماند. همچنین وقتی دو متغیر به یک شیء تغییرپذیر اشاره می‌کنند، تغییر از طریق یکی روی دیگری هم تأثیر می‌گذارد.

### مثال ۲: تأثیر روی حافظه و بهینه‌سازی

```python
# ============ MEMORY OPTIMIZATION ============

print("=== Memory Optimization with Immutability ===\n")

# Python caches small integers and some strings
a = 100
b = 100
print(f"a = 100, b = 100")
print(f"id(a): {id(a)}, id(b): {id(b)}")
print(f"Same object? {a is b}")
print("Python reuses the same integer object for efficiency\n")

# String interning (for certain strings)
str1 = "hello"
str2 = "hello"
print(f'str1 = "hello", str2 = "hello"')
print(f'id(str1): {id(str1)}, id(str2): {id(str2)}')
print(f"Same object? {str1 is str2}")
print("Python interns certain strings for efficiency\n")

# But not all strings are interned
str3 = "hello world"
str4 = "hello world"
print(f'str3 = "hello world", str4 = "hello world"')
print(f'id(str3): {id(str3)}, id(str4): {id(str4)}')
print(f"Same object? {str3 is str4}")
print("Longer strings may not be interned automatically\n")


# ============ FUNCTION BEHAVIOR ============

print("\n=== Function Behavior with Mutable/Immutable ===\n")

# Function with immutable parameter
def modify_number(n):
    """Try to modify an integer"""
    n = n * 2
    print(f"Inside function, n: {n}, id(n): {id(n)}")
    return n

original_num = 10
print(f"Before function call: {original_num}, id: {id(original_num)}")
modify_number(original_num)
print(f"After function call: {original_num}, id: {id(original_num)}")
print("Original unchanged! Integer is immutable.\n")

# Function with mutable parameter
def modify_list(lst):
    """Modify a list in place"""
    lst.append(999)
    print(f"Inside function, lst: {lst}, id(lst): {id(lst)}")

original_list = [1, 2, 3]
print(f"Before function call: {original_list}, id: {id(original_list)}")
modify_list(original_list)
print(f"After function call: {original_list}, id: {id(original_list)}")
print("Original CHANGED! List is mutable.\n")

# Safe pattern: Create copy before passing to function
def safe_modify_list(lst):
    """Create a copy to avoid modifying original"""
    lst_copy = lst.copy()
    lst_copy.append(999)
    return lst_copy

safe_list = [1, 2, 3]
result = safe_modify_list(safe_list)
print(f"Original (safe): {safe_list}")
print(f"Returned copy: {result}")
print("Original preserved by using copy!\n")


# ============ NESTED STRUCTURES ============

print("\n=== Nested Structures ===\n")

# Tuple with mutable element (important edge case)
nested_tuple = (1, 2, [3, 4, 5])
print(f"Nested tuple: {nested_tuple}")
print(f"Tuple id: {id(nested_tuple)}")
print(f"Inner list id: {id(nested_tuple[2])}")

# Can we modify the inner list?
nested_tuple[2].append(6)
print(f"\nAfter appending to inner list: {nested_tuple}")
print(f"Inner list id after modification: {id(nested_tuple[2])}")
print("The TUPLE didn't change (still points to same list)")
print("But the LIST inside it DID change (mutable)!")

# This is why truly immutable structures need all elements immutable
truly_immutable = (1, 2, (3, 4, 5))
print(f"\nTruly immutable tuple: {truly_immutable}")
try:
    truly_immutable[2][0] = 999
except TypeError as e:
    print(f"Cannot modify even nested elements: {e}")
```

**تحلیل کد:**
پایتون برای بهینه‌سازی حافظه، اشیاء تغییرناپذیر کوچک (مثل اعداد کوچک و برخی رشته‌ها) را cache می‌کند و چندین متغیر به یک شیء اشاره می‌کنند. در توابع، پارامترهای تغییرناپذیر ایمن هستند اما پارامترهای تغییرپذیر می‌توانند توسط تابع تغییر کنند. برای جلوگیری از این، می‌توانید از کپی استفاده کنید. همچنین توجه کنید که یک تاپل می‌تواند حاوی اشیاء تغییرپذیر باشد که خود قابل تغییر هستند.

## تمرین (Exercise)

### تمرین ۱
تابعی بنویسید که یک لیست دریافت کند و بدون تغییر لیست اصلی، نسخه‌ای مرتب‌شده از آن را برگرداند. سپس نشان دهید که لیست اصلی تغییر نکرده است.

### تمرین ۲
کدی بنویسید که نشان دهد چرا نباید از لیست به عنوان مقدار پیش‌فرض پارامتر تابع استفاده کرد (مشکل mutable default argument).

---

<details>
<summary>پاسخ تشریحی تمرین‌ها</summary>

```python
# Exercise 1 Solution
def sorted_copy(input_list):
    """Return sorted copy without modifying original"""
    # Method 1: Using sorted() function
    return sorted(input_list)
    
    # Method 2: Using copy and sort
    # list_copy = input_list.copy()
    # list_copy.sort()
    # return list_copy

# Test the function
original = [5, 2, 8, 1, 9, 3]
print(f"Original before: {original}")
sorted_result = sorted_copy(original)
print(f"Sorted result: {sorted_result}")
print(f"Original after: {original}")
print(f"Original unchanged: {original == [5, 2, 8, 1, 9, 3]}")


# Exercise 2 Solution - Demonstrating mutable default argument problem

# BAD PATTERN - Don't do this!
def bad_add_item(item, target_list=[]):
    """This function has a bug due to mutable default argument"""
    target_list.append(item)
    return target_list

print("=== Bad Pattern (Mutable Default Argument) ===")
print(f"First call: {bad_add_item(1)}")
print(f"Second call: {bad_add_item(2)}")
print(f"Third call: {bad_add_item(3)}")
print("Problem: All calls share the SAME list!\n")

# GOOD PATTERN - Do this instead!
def good_add_item(item, target_list=None):
    """Correct pattern using None as default"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

print("=== Good Pattern (None Default) ===")
print(f"First call: {good_add_item(1)}")
print(f"Second call: {good_add_item(2)}")
print(f"Third call: {good_add_item(3)}")
print("Each call gets a fresh list!")
```

</details>

## جمع‌بندی

- ✅ **اشیاء تغییرناپذیر (Immutable)**: int, float, str, tuple, frozenset
- ✅ **اشیاء تغییرپذیر (Mutable)**: list, dict, set
- ✅ تغییر اشیاء تغییرناپذیر = ایجاد شیء جدید در حافظه
- ✅ تغییر اشیاء تغییرپذیر = تغییر در محل (in-place)
- ✅ پایتون اشیاء تغییرناپذیر کوچک را cache می‌کند (بهینه‌سازی حافظه)
- ✅ فقط اشیاء تغییرناپذیر **هش‌پذیر (Hashable)** هستند
- ✅ هنگام پاس دادن اشیاء تغییرپذیر به توابع مراقب باشید
- ✅ برای ایمن‌سازی، از کپی (`copy()` یا `[:]`) استفاده کنید
- ✅ هرگز از شیء تغییرپذیر به عنوان مقدار پیش‌فرض پارامتر استفاده نکنید
- ✅ تاپل با عنصر تغییرپذیر = تاپل تغییرناپذیر است ولی عنصر داخلی قابل تغییر است
