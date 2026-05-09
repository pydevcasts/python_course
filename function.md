
## ✅ 1️⃣ شمارش تکرار عناصر لیست

```python
arr = ["a", "b", "f", "a", "b", "a"]
demo = {}

for i in arr:
    if i in demo:
        demo[i] +=1
    else:
        demo[i] = 1

max_val = max(demo.values())

for key, val in demo.items():
    if val == max_val:
        print(key)
```

### چه اتفاقی می‌افتد؟

دیکشنری ساخته می‌شود:

```python
{'a': 3, 'b': 2, 'f': 1}
```

بیشترین مقدار = `3`

✅ خروجی:

```
a
```

---

## ✅ 2️⃣ تابع ساده

```python
def foo():
    return(1)

foo()
```

✅ مقدار برمی‌گرداند:  
```
1
```
ولی چون `print` نکردی، چیزی نمایش داده نمی‌شود.

---

## ✅ 3️⃣ استفاده از متغیر سراسری در تابع

```python
arr = "aboli"

def showName():
    return arr.upper()

showName()
```

✅ خروجی:
```
'ABOLI'
```

---

## ✅ 4️⃣ تغییر متغیر global

```python
name  = "hamed"

def foo():
    global name
    name = "aboli"
    return name

foo()
print(name)
```

چون از `global` استفاده کردی، مقدار اصلی تغییر می‌کند.

✅ خروجی:
```
aboli
```

---

## ✅ 5️⃣ مثال دیگر global

```python
x = 5

def master():
    global x
    x = 9
    return x + 10

master()
print(x + 20)
```

داخل تابع مقدار x می‌شود 9.

پس:

```
9 + 20 = 29
```

✅ خروجی:
```
29
```

---

## ✅ 6️⃣ تابع با پارامتر

```python
def b(name):
    return name

b("hamed")
```

✅ مقدار:
```
"hamed"
```

---

## ✅ 7️⃣ جمع سه عدد

```python
def name(x, y, z):
    return x + y + z

name(5,6,8)
```

✅ خروجی:
```
19
```

---

## ✅ 8️⃣ استفاده از f-string

```python
def showname(name, family):
    return f'my name is: {name} and my family is: {family}'

showname('kolsoum', 'akbari')
```

✅ خروجی:
```
my name is: kolsoum and my family is: akbari
```

---

## ✅ 9️⃣ بررسی وجود مقدار در لیست

```python
def barker(x):
    if "kolsoum" in x:
        return True
    else:
        return False

y = ['kolsoum', 'jalal', 'sogand']
barker(y)
```

✅ خروجی:
```
True
```

(می‌توانستی کوتاه‌تر بنویسی:)

```python
return "kolsoum" in x
```

---

## ✅ 10️⃣ پیدا کردن ایندکس

```python
def indexof(name):
    return name.index("m")

x = "hamed seyedi"
indexof(x)
```

✅ اولین m در موقعیت:

```
2
```

---

## ✅ 11️⃣ برعکس کردن رشته

```python
def indexof(name):
    return name[-1::-1]

x = "hamed seyedi"
indexof(x)
```

✅ خروجی:
```
"ideyes demah"
```

روش ساده‌تر:

```python
return name[::-1]
```

---

## ✅ 12️⃣ بررسی اعداد بزرگ‌تر از 30

```python
def counter(x):
    for i in arr:
        if i > 30:
            print(i)

arr= [10,20,30,40,50,55,42]
counter(arr)
```

✅ خروجی:
```
40
50
55
42
```

🔴 نکته مهم:  
داخل تابع از `arr` استفاده کردی نه `x`.  
بهتر و اصولی‌تر:

```python
def counter(x):
    for i in x:
        if i > 30:
            print(i)
```

---

# ✅ نکات مهمی که از این تمرین یاد گرفتی:

- دیکشنری برای شمارش عالیه ✅
- `global` باعث تغییر متغیر اصلی می‌شود ✅
- توابع بدون `print` چیزی نمایش نمی‌دهند ✅
- اسلایس `[::-1]` رشته را برعکس می‌کند ✅
- همیشه داخل تابع از پارامتر استفاده کن نه متغیر بیرونی ✅

---

