# صفحه ۱۸: ست و فروزن‌ست (Sets & Frozensets) - عملیات ریاضی مجموعه‌ها، تفاوت mutable و immutable

## هدف آموزشی
در این صفحه با دو ساختار داده ست (Set) و فروزن‌ست (Frozenset) آشنا می‌شوید. یاد می‌گیرید چگونه از عملیات ریاضی مجموعه‌ها استفاده کنید و تفاوت‌های کلیدی بین نسخه تغییرپذیر و تغییرناپذیر را درک نمایید.

## توضیح مفهومی

**ست (Set)** یک ساختار داده **تغییرپذیر (Mutable)**، **نامرتب (Unordered)** و **بدون عنصر تکراری (Unique Elements)** در پایتون است. ست‌ها بر اساس نظریه مجموعه‌های ریاضی طراحی شده‌اند و برای عملیات_membership_ (بررسی عضویت) و عملیات مجموعه‌ای بسیار کارآمد هستند.

**فروزن‌ست (Frozenset)** نسخه **تغییرناپذیر (Immutable)** ست است. پس از ایجاد فروزن‌ست، نمی‌توان آن را تغییر داد. این ویژگی باعث می‌شود فروزن‌ست‌ها **هش‌پذیر (Hashable)** باشند و بتوانند به عنوان کلید دیکشنری یا عضو سایر ست‌ها استفاده شوند.

### ویژگی‌های کلیدی

| ویژگی | Set | Frozenset |
|-------|-----|-----------|
| تغییرپذیری | ✅ بله | ❌ خیر |
| هش‌پذیری | ❌ خیر | ✅ بله |
| ترتیب عناصر | نامرتب | نامرتب |
| عناصر تکراری | حذف می‌شوند | حذف می‌شوند |
| عملکرد | سریع | سریع |

### عملیات مجموعه‌ای

- **اتحاد (Union)**: تمام عناصر هر دو مجموعه
- **اشتراک (Intersection)**: عناصر مشترک بین دو مجموعه
- **تفاضل (Difference)**: عناصر موجود در یک مجموعه ولی نه در دیگری
- **تفاضل متقارن (Symmetric Difference)**: عناصری که فقط در یکی از دو مجموعه هستند

## بخش کد عملی

### مثال ۱: کار با Set و عملیات پایه

```python
# Create sets in different ways
fruits = {"apple", "banana", "cherry", "orange"}
vegetables = set(["carrot", "broccoli", "spinach", "apple"])

print(f"Fruits: {fruits}")
print(f"Vegetables: {vegetables}")

# Note: Duplicate elements are automatically removed
numbers_with_duplicates = [1, 2, 3, 2, 4, 3, 5]
unique_numbers = set(numbers_with_duplicates)
print(f"\nOriginal list: {numbers_with_duplicates}")
print(f"As set (unique): {unique_numbers}")

# Add elements to set (mutable operation)
fruits.add("grape")
print(f"\nAfter adding grape: {fruits}")

# Add multiple elements
fruits.update(["kiwi", "mango"])
print(f"After update: {fruits}")

# Remove elements
fruits.remove("banana")  # Raises error if not found
fruits.discard("cherry")  # No error if not found
removed_item = fruits.pop()  # Removes and returns arbitrary element
print(f"After remove/discard/pop: {fruits}")
print(f"Popped item: {removed_item}")

# Check membership
is_apple_in_fruits = "apple" in fruits
is_watermelon_in_fruits = "watermelon" in fruits
print(f"\nIs apple in fruits? {is_apple_in_fruits}")
print(f"Is watermelon in fruits? {is_watermelon_in_fruits}")

# Set length
print(f"Number of fruits: {len(fruits)}")

# Clear the set
fruits_copy = fruits.copy()
fruits_copy.clear()
print(f"\nAfter clear: {fruits_copy}")
```

**تحلیل کد:**
در این مثال، روش‌های مختلف ایجاد ست را مشاهده می‌کنید. ست‌ها به طور خودکار عناصر تکراری را حذف می‌کنند. متد `add()` یک عنصر اضافه می‌کند، `update()` چندین عنصر را می‌افزاید. متد `remove()` اگر عنصر وجود نداشته باشد خطا می‌دهد، اما `discard()` خطا نمی‌دهد. متد `pop()` یک عنصر دلخواه را حذف و برمی‌گرداند (چون ست نامرتب است، مشخص نیست کدام عنصر حذف می‌شود).

### مثال ۲: عملیات ریاضی مجموعه‌ها

```python
# Define two sets for operations
set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union - all elements from both sets
union_result = set_a.union(set_b)
union_operator = set_a | set_b
print(f"\nUnion (A ∪ B): {union_result}")
print(f"Union with operator: {union_operator}")

# Intersection - elements in both sets
intersection_result = set_a.intersection(set_b)
intersection_operator = set_a & set_b
print(f"\nIntersection (A ∩ B): {intersection_result}")
print(f"Intersection with operator: {intersection_operator}")

# Difference - elements in A but not in B
difference_result = set_a.difference(set_b)
difference_operator = set_a - set_b
print(f"\nDifference (A - B): {difference_result}")
print(f"Difference with operator: {difference_operator}")

# Symmetric Difference - elements in either A or B but not both
symmetric_diff_result = set_a.symmetric_difference(set_b)
symmetric_diff_operator = set_a ^ set_b
print(f"\nSymmetric Difference (A △ B): {symmetric_diff_result}")
print(f"Symmetric Difference with operator: {symmetric_diff_operator}")

# Subset and Superset checks
small_set = {1, 2, 3}
print(f"\nIs {small_set} a subset of A? {small_set.issubset(set_a)}")
print(f"Is A a superset of {small_set}? {set_a.issuperset(small_set)}")

# Disjoint check (no common elements)
disjoint_set = {10, 11, 12}
print(f"Is A disjoint with {disjoint_set}? {set_a.isdisjoint(disjoint_set)}")

# Practical example: Find common users between two platforms
platform_a_users = {"alice", "bob", "charlie", "david"}
platform_b_users = {"charlie", "david", "eve", "frank"}

common_users = platform_a_users.intersection(platform_b_users)
unique_to_a = platform_a_users.difference(platform_b_users)
unique_to_b = platform_b_users.difference(platform_a_users)
all_users = platform_a_users.union(platform_b_users)

print(f"\nCommon users: {common_users}")
print(f"Only on Platform A: {unique_to_a}")
print(f"Only on Platform B: {unique_to_b}")
print(f"All unique users: {all_users}")
```

**تحلیل کد:**
این مثال عملیات اصلی مجموعه‌ها را نشان می‌دهد. هر عملیات هم با متد و هم با اپراتور قابل انجام است. اتحاد (`|`) همه عناصر را ترکیب می‌کند، اشتراک (`&`) عناصر مشترک را پیدا می‌کند، تفاضل (`-`) عناصر یک مجموعه را بدون عناصر مجموعه دیگر برمی‌گرداند، و تفاضل متقارن (`^`) عناصری را برمی‌گرداند که فقط در یکی از دو مجموعه هستند.

### مثال ۳: Frozenset و کاربردهای آن

```python
# Create frozensets
frozen_fruits = frozenset(["apple", "banana", "cherry"])
frozen_vegetables = frozenset(["carrot", "broccoli", "apple"])

print(f"Frozen Fruits: {frozen_fruits}")
print(f"Frozen Vegetables: {frozen_vegetables}")

# Try to modify frozenset (will cause error)
try:
    frozen_fruits.add("grape")
    print("Modification succeeded")
except AttributeError as e:
    print(f"\nError when modifying frozenset: {e}")

# Frozenset operations (same as set)
frozen_union = frozen_fruits.union(frozen_vegetables)
frozen_intersection = frozen_fruits.intersection(frozen_vegetables)
print(f"\nUnion: {frozen_union}")
print(f"Intersection: {frozen_intersection}")

# Use frozenset as dictionary key (because it's hashable)
location_data = {
    frozenset(["latitude", "longitude"]): "Geographic Coordinates",
    frozenset(["x", "y"]): "Cartesian Coordinates",
    frozenset(["red", "green", "blue"]): "RGB Color Model"
}

search_key = frozenset(["latitude", "longitude"])
print(f"\nData for {search_key}: {location_data[search_key]}")

# Frozenset in a set (nested sets)
set_of_sets = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([1, 2])  # This is a subset
}

print(f"\nSet of frozensets: {set_of_sets}")

# Convert between set and frozenset
mutable_set = set(frozen_fruits)
mutable_set.add("new_item")
print(f"\nConverted to set and modified: {mutable_set}")

back_to_frozen = frozenset(mutable_set)
print(f"Converted back to frozenset: {back_to_frozen}")

# Performance comparison for membership testing
import time

large_list = list(range(100000))
large_set = set(large_list)
large_frozenset = frozenset(large_list)

# Test membership in list
start = time.time()
99999 in large_list
list_time = time.time() - start

# Test membership in set
start = time.time()
99999 in large_set
set_time = time.time() - start

# Test membership in frozenset
start = time.time()
99999 in large_frozenset
frozen_time = time.time() - start

print(f"\nMembership test time:")
print(f"  List: {list_time:.6f} seconds")
print(f"  Set: {set_time:.6f} seconds")
print(f"  Frozenset: {frozen_time:.6f} seconds")
print(f"  Set is {list_time/set_time:.0f}x faster than list!")
```

**تحلیل کد:**
فروزن‌ست‌ها غیرقابل تغییر هستند و بنابراین متدهایی مانند `add()` یا `remove()` ندارند. اما تمام عملیات مجموعه‌ای را پشتیبانی می‌کنند و نتیجه را به صورت فروزن‌ست جدید برمی‌گردانند. مهم‌ترین مزیت فروزن‌ست، هش‌پذیر بودن آن است که امکان استفاده به عنوان کلید دیکشنری یا عضو ست‌های دیگر را فراهم می‌کند. همچنین ست و فروزن‌ست برای تست عضویت بسیار سریع‌تر از لیست هستند.

## تمرین (Exercise)

### تمرین ۱
دو ست از اعداد صحیح ایجاد کنید:
- ست اول: اعداد ۱ تا ۱۰
- ست دوم: اعداد ۵ تا ۱۵

سپس موارد زیر را محاسبه کنید:
- اعدادی که فقط در ست اول هستند
- اعدادی که فقط در ست دوم هستند
- اعدادی که در هر دو ست هستند
- تمام اعداد یکتا از هر دو ست

### تمرین ۲
تابعی بنویسید که یک لیست از رشته‌ها دریافت کند و بررسی کند آیا تمام رشته‌ها منحصر به فرد هستند یا خیر (با استفاده از ست).

---

<details>
<summary>پاسخ تشریحی تمرین‌ها</summary>

```python
# Exercise 1 Solution
# Create two sets
set_first = set(range(1, 11))  # 1 to 10
set_second = set(range(5, 16))  # 5 to 15

print(f"Set 1 (1-10): {set_first}")
print(f"Set 2 (5-15): {set_second}")

# Only in first set
only_first = set_first.difference(set_second)
print(f"\nOnly in Set 1: {only_first}")

# Only in second set
only_second = set_second.difference(set_first)
print(f"Only in Set 2: {only_second}")

# In both sets (intersection)
both_sets = set_first.intersection(set_second)
print(f"In both sets: {both_sets}")

# All unique numbers (union)
all_unique = set_first.union(set_second)
print(f"All unique numbers: {all_unique}")


# Exercise 2 Solution
def are_all_unique(string_list):
    """Check if all strings in list are unique"""
    unique_strings = set(string_list)
    return len(unique_strings) == len(string_list)

# Test the function
test_list_1 = ["apple", "banana", "cherry", "apple"]
test_list_2 = ["apple", "banana", "cherry", "date"]

print(f"List 1: {test_list_1}")
print(f"All unique? {are_all_unique(test_list_1)}")

print(f"\nList 2: {test_list_2}")
print(f"All unique? {are_all_unique(test_list_2)}")
```

</details>

## جمع‌بندی

- ✅ **ست (Set)** ساختار داده **تغییرپذیر (Mutable)**، نامرتب و بدون عناصر تکراری است
- ✅ **فروزن‌ست (Frozenset)** نسخه **تغییرناپذیر (Immutable)** ست است
- ✅ ست‌ها هش‌پذیر نیستند، اما فروزن‌ست‌ها هش‌پذیر هستند
- ✅ فروزن‌ست می‌تواند به عنوان کلید دیکشنری استفاده شود
- ✅ عملیات مجموعه‌ای: اتحاد (`|`)، اشتراک (`&`)، تفاضل (`-`)، تفاضل متقارن (`^`)
- ✅ ست و فروزن‌ست برای تست عضویت (`in`) بسیار سریع‌تر از لیست هستند
- ✅ ست‌ها متدهای `add()`، `remove()`، `discard()`، `pop()` را پشتیبانی می‌کنند
- ✅ فروزن‌ست‌ها هیچ متد تغییردهنده‌ای ندارند
- ✅ می‌توان بین ست و فروزن‌ست تبدیل انجام داد
- ✅ از ست برای حذف عناصر تکراری از لیست استفاده می‌شود
