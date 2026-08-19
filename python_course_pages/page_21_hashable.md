# صفحه ۲۱: هش‌پذیر بودن (Hashable) - مفهوم هش، چرا کلیدهای دیکشنری باید هش‌پذیر باشند، رابطه با immutability

## هدف آموزشی
در این صفحه با مفهوم هش‌پذیری (Hashability) در پایتون آشنا می‌شوید. یاد می‌گیرید تابع `hash()` چگونه کار می‌کند، چرا کلیدهای دیکشنری و اعضای ست باید هش‌پذیر باشند، و چه رابطه‌ای بین تغییرناپذیری و هش‌پذیری وجود دارد.

## توضیح مفهومی

**هش‌پذیری (Hashability)** قابلیتی است که به یک شیء اجازه می‌دهد مقدار هش ثابتی داشته باشد که در طول عمر آن شیء تغییر نمی‌کند. این مقدار هش یک عدد صحیح است که توسط تابع `hash()` محاسبه می‌شود.

### چرا هش مهم است؟

دیکشنری‌ها و ست‌ها برای دسترسی سریع به داده‌ها از ساختاری به نام **جدول هش (Hash Table)** استفاده می‌کنند. وقتی شما یک کلید را در دیکشنری جستجو می‌کنید:

1. پایتون تابع `hash()` را روی کلید فراخوانی می‌کند
2. مقدار هش به عنوان ایندکس در جدول هش استفاده می‌شود
3. دسترسی به مقدار مربوطه در زمان O(1) انجام می‌شود (بسیار سریع!)

### شرایط هش‌پذیری

یک شیء برای هش‌پذیر بودن باید دو شرط داشته باشد:

1. **متد `__hash__()`:** باید مقدار هش صحیح و ثابت برگرداند
2. **متد `__eq__()`:** باید بتواند برابری با اشیاء دیگر را بررسی کند

### رابطه با تغییرناپذیری (Immutability)

- ✅ تمام اشیاء **تغییرناپذیر (Immutable)** استاندارد پایتون هش‌پذیر هستند
- ❌ تمام اشیاء **تغییرپذیر (Mutable)** استاندارد پایتون هش‌ناپذیر هستند
- ⚠️ یک شیء custom می‌تواند هم تغییرپذیر باشد و هم هش‌پذیر (اما توصیه نمی‌شود)

**چرا اشیاء تغییرپذیر نباید هش‌پذیر باشند؟**
اگر یک شیء پس از ایجاد تغییر کند، مقدار هش آن ممکن است تغییر کند. این باعث می‌شود که دیگر نتوان آن را در جدول هش پیدا کرد!

## بخش کد عملی

### مثال ۱: بررسی Hashability اشیاء مختلف

```python
# ============ CHECKING HASHABILITY ============

print("=== Checking Hashability of Different Objects ===\n")

def check_hashability(obj, name):
    """Check if an object is hashable"""
    try:
        hash_value = hash(obj)
        print(f"{name}:")
        print(f"  Value: {obj}")
        print(f"  Hash: {hash_value}")
        print(f"  Is hashable? ✅ Yes")
    except TypeError as e:
        print(f"{name}:")
        print(f"  Value: {obj}")
        print(f"  Error: {e}")
        print(f"  Is hashable? ❌ No")
    print()


# Immutable objects (should be hashable)
check_hashability(42, "Integer")
check_hashability(3.14, "Float")
check_hashability("Hello", "String")
check_hashability((1, 2, 3), "Tuple with immutable elements")

# Mutable objects (should NOT be hashable)
check_hashability([1, 2, 3], "List")
check_hashability({"key": "value"}, "Dictionary")
check_hashability({1, 2, 3}, "Set")

# Special cases
check_hashability(None, "None")
check_hashability(True, "Boolean")
check_hashability(frozenset([1, 2, 3]), "Frozenset")

# Tuple with mutable element (NOT hashable!)
check_hashability((1, 2, [3, 4]), "Tuple with list inside")


# ============ HASH CONSISTENCY ============

print("\n=== Hash Consistency ===\n")

# Same value = same hash
text1 = "Python"
text2 = "Python"

print(f'text1 = "Python"')
print(f'text2 = "Python"')
print(f"hash(text1): {hash(text1)}")
print(f"hash(text2): {hash(text2)}")
print(f"Same hash? {hash(text1) == hash(text2)}")
print(f"Same object? {text1 is text2}")
print("Equal values always have equal hashes!\n")

# Different values usually have different hashes
text3 = "Java"
print(f'hash("Python"): {hash(text1)}')
print(f'hash("Java"): {hash(text3)}')
print("Different values typically have different hashes")
```

**تحلیل کد:**
این مثال نشان می‌دهد که اشیاء تغییرناپذیر مانند اعداد، رشته‌ها و تاپل‌های با عناصر تغییرناپذیر هش‌پذیر هستند. اما اشیاء تغییرپذیر مانند لیست، دیکشنری و ست هش‌ناپذیرند. نکته مهم: تاپلی که حاوی لیست باشد نیز هش‌ناپذیر است، زیرا عنصر داخلی قابل تغییر است. اشیاء با مقدار برابر همیشه هش برابر دارند.

### مثال ۲: کلیدهای دیکشنری و اعضای ست

```python
# ============ DICTIONARY KEYS ============

print("=== Dictionary Keys ===\n")

# Valid keys (hashable)
valid_dict = {
    "string_key": "value1",
    42: "value2",
    3.14: "value3",
    (1, 2): "value4",
    None: "value5",
    True: "value6"
}

print("Dictionary with various hashable keys:")
for key, value in valid_dict.items():
    print(f"  {repr(key)} ({type(key).__name__}): {value}")

# Try to use mutable object as key (will fail!)
print("\nTrying to use list as key:")
try:
    invalid_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"  Error: {e}")
    print("  Lists cannot be dictionary keys!")

# But tuple with mutable element also fails
print("\nTrying to use tuple with list as key:")
try:
    invalid_tuple_key = {(1, 2, [3, 4]): "value"}
except TypeError as e:
    print(f"  Error: {e}")
    print("  Even tuples with mutable elements cannot be keys!")


# ============ SET MEMBERS ============

print("\n=== Set Members ===\n")

# Valid set members (hashable)
valid_set = {1, 2, 3, "hello", (4, 5)}
print(f"Valid set: {valid_set}")

# Try to add mutable object to set
print("\nTrying to add list to set:")
try:
    invalid_set = {1, 2, [3, 4]}
except TypeError as e:
    print(f"  Error: {e}")
    print("  Lists cannot be set members!")

# Frozenset can be a set member
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(f"\nSet with frozensets: {nested_set}")


# ============ PRACTICAL EXAMPLE ============

print("\n=== Practical Example: Using Tuple as Key ===\n")

# Store coordinates as dictionary keys
location_data = {
    (40.7128, -74.0060): "New York City",
    (51.5074, -0.1278): "London",
    (48.8566, 2.3522): "Paris",
    (35.6762, 139.6503): "Tokyo"
}

print("Location database:")
for coords, city in location_data.items():
    print(f"  {coords}: {city}")

# Look up a location
search_coords = (51.5074, -0.1278)
print(f"\nLooking up {search_coords}:")
print(f"  Found: {location_data.get(search_coords, 'Not found')}")

# Why not use list as key?
print("\nWhy not list as key?")
print("Because [40.7128, -74.0060] could change to [40.7128, -74.0000]")
print("Then the hash would change and we couldn't find the data!")
```

**تحلیل کد:**
دیکشنری‌ها و ست‌ها فقط اشیاء هش‌پذیر را به عنوان کلید یا عضو می‌پذیرند. تاپل‌ها گزینه عالی برای کلیدهای مرکب هستند (مثل مختصات جغرافیایی). اگر اشیاء تغییرپذیر مجاز بودند، با تغییر آن‌ها مقدار هش تغییر می‌کرد و داده‌ها غیرقابل دسترس می‌شدند.

### مثال ۳: رابطه Immutability و Hashability

```python
# ============ IMMUTABILITY AND HASH RELATIONSHIP ============

print("=== Immutability and Hash Relationship ===\n")

# String hash stays constant
text = "Hello"
original_hash = hash(text)
print(f'Original string: "{text}"')
print(f"Original hash: {original_hash}")

# Strings are immutable, so hash never changes
# We can't modify the string, only create new ones
text = text + " World"  # Creates NEW string object
print(f'\nNew string: "{text}"')
print(f"New hash: {hash(text)}")
print("The original string object still has the same hash!\n")

# Compare with list (mutable, unhashable)
print("Lists are mutable:")
my_list = [1, 2, 3]
print(f"Original list: {my_list}")
print(f"List id: {id(my_list)}")

my_list.append(4)
print(f"After append: {my_list}")
print(f"List id (same object): {id(my_list)}")
print("The list changed but id stayed same - this is why it can't be hashed!\n")


# ============ CUSTOM CLASS HASHABILITY ============

print("=== Custom Class Hashability ===\n")

class Person:
    """A class with default hash behavior"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


# Default: objects are hashable by identity
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)

print(f"person1: {person1}")
print(f"person2: {person2}")
print(f"person1 == person2: {person1 == person2}")
print(f"hash(person1): {hash(person1)}")
print(f"hash(person2): {hash(person2)}")
print("Different objects have different hashes even with same data\n")

# Can use as dictionary keys (but based on identity, not value)
person_dict = {person1: "First person"}
print(f"person_dict[person1]: {person_dict[person1]}")
# print(person_dict[person2])  # KeyError! Different object


# Custom hash based on value
class HashablePerson:
    """A class with custom hash based on value"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __hash__(self):
        # Hash based on immutable attributes
        return hash((self.name, self.age))
    
    def __eq__(self, other):
        # Equality must match hash
        if isinstance(other, HashablePerson):
            return (self.name, self.age) == (other.name, other.age)
        return False
    
    def __repr__(self):
        return f"HashablePerson('{self.name}', {self.age})"


hperson1 = HashablePerson("Bob", 25)
hperson2 = HashablePerson("Bob", 25)

print(f"\nhperson1: {hperson1}")
print(f"hperson2: {hperson2}")
print(f"hperson1 == hperson2: {hperson1 == hperson2}")
print(f"hash(hperson1): {hash(hperson1)}")
print(f"hash(hperson2): {hash(hperson2)}")
print(f"Same hash? {hash(hperson1) == hash(hperson2)}")

# Now they work as equivalent dictionary keys
hperson_dict = {hperson1: "Bob's data"}
print(f"\nhperson_dict[hperson1]: {hperson_dict[hperson1]}")
print(f"hperson_dict[hperson2]: {hperson_dict[hperson2]}")
print("Now objects with same value are interchangeable as keys!")


# ============ WARNING: Mutable with Hash ============

print("\n=== Warning: Don't Make Mutable Objects Hashable ===\n")

class BadIdea:
    """DON'T DO THIS - mutable object with custom hash"""
    
    def __init__(self, value):
        self.value = value
    
    def __hash__(self):
        return hash(self.value)
    
    def __repr__(self):
        return f"BadIdea({self.value})"


bad_obj = BadIdea(100)
print(f"Created: {bad_obj}")
print(f"Initial hash: {hash(bad_obj)}")

# Use as dictionary key
bad_dict = {bad_obj: "Some data"}
print(f"Added to dictionary")

# Now mutate the object
bad_obj.value = 200
print(f"\nAfter mutation: {bad_obj}")
print(f"New hash: {hash(bad_obj)}")

# Try to access from dictionary
print(f"\nTrying to access bad_dict[bad_obj]...")
try:
    result = bad_dict[bad_obj]
    print(f"Found: {result}")
except KeyError:
    print("KeyError! Object is lost in the dictionary!")
    print("The hash changed, so Python looks in wrong place!")

print("\nThis is why mutable objects should NOT be hashable!")
```

**تحلیل کد:**
به صورت پیش‌فرض، اشیاء کلاس‌های custom بر اساس هویت (identity) هش می‌شوند. می‌توان با تعریف متد `__hash__()` و `__eq__()` رفتار سفارشی ایجاد کرد. اما هرگز نباید اشیاء تغییرپذیر را هش‌پذیر کرد، زیرا با تغییر شیء، هش آن تغییر کرده و در دیکشنری گم می‌شود!

## تمرین (Exercise)

### تمرین ۱
کلاسی به نام `Point` بنویسید که نمایانگر یک نقطه دو بعدی با مختصات x و y باشد. کلاس باید:
- تغییرناپذیر باشد (attributes نباید پس از ایجاد تغییر کنند)
- هش‌پذیر باشد بر اساس x و y
- دو نقطه با مختصات یکسان برابر و دارای هش یکسان باشند

### تمرین ۲
چرا نمی‌توانیم از یک لیست به عنوان کلید دیکشنری استفاده کنیم؟ راه حل چیست؟ کدی بنویسید که این موضوع را نشان دهد.

---

<details>
<summary>پاسخ تشریحی تمرین‌ها</summary>

```python
# Exercise 1 Solution
class Point:
    """Immutable 2D point that is hashable"""
    
    def __init__(self, x, y):
        # Use __slots__ for extra immutability and memory efficiency
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    # Prevent modification (optional extra safety)
    def __setattr__(self, name, value):
        raise AttributeError("Point is immutable!")


# Test the Point class
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(5, 6)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")

print(f"\np1 == p2: {p1 == p2}")
print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}")

# Use as dictionary key
point_dict = {p1: "First point", p3: "Third point"}
print(f"\npoint_dict[p1]: {point_dict[p1]}")
print(f"point_dict[p2]: {point_dict[p2]}")  # Works because p1 == p2

# Try to modify (will fail)
try:
    p1.x = 10
except AttributeError as e:
    print(f"\nCannot modify: {e}")


# Exercise 2 Solution
print("=== Why List Cannot Be Dictionary Key ===\n")

# Problem demonstration
print("Problem: Lists are mutable")
my_list = [1, 2, 3]
print(f"Created list: {my_list}")

try:
    my_dict = {my_list: "value"}
    print("Successfully used list as key")
except TypeError as e:
    print(f"Error: {e}")

print("\nReason: If lists were hashable...")
print("1. Create dict with list key: {[1, 2, 3]: 'value'}")
print("2. Mutate list: list becomes [1, 2, 3, 4]")
print("3. Hash changes, can't find the value anymore!")

print("\n=== Solution: Use Tuple Instead ===\n")

# Solution: Convert to tuple (immutable)
my_tuple = tuple([1, 2, 3])
print(f"Convert list to tuple: {my_tuple}")

valid_dict = {my_tuple: "value"}
print(f"Successfully created dict: {valid_dict}")

# Or use frozenset if order doesn't matter
my_frozenset = frozenset([1, 2, 3])
another_dict = {my_frozenset: "unordered value"}
print(f"Using frozenset: {another_dict}")
```

</details>

## جمع‌بندی

- ✅ **هش‌پذیر (Hashable)**: شیئی با مقدار هش ثابت در طول عمر
- ✅ تابع `hash()` مقدار هش integer برمی‌گرداند
- ✅ دیکشنری‌ها و ست‌ها از جدول هش برای دسترسی O(1) استفاده می‌کنند
- ✅ تمام اشیاء **تغییرناپذیر** استاندارد هش‌پذیر هستند
- ✅ تمام اشیاء **تغییرپذیر** استاندارد هش‌ناپذیر هستند
- ✅ کلیدهای دیکشنری و اعضای ست باید هش‌پذیر باشند
- ✅ تاپل فقط اگر همه عناصرش هش‌پذیر باشند، هش‌پذیر است
- ✅ اشیاء custom با `__hash__()` و `__eq__()` قابل تنظیم هستند
- ✅ ⚠️ هرگز اشیاء تغییرپذیر را هش‌پذیر نکنید (باعث گم شدن داده می‌شود)
- ✅ راه حل استفاده از لیست به عنوان کلید: تبدیل به tuple یا frozenset
