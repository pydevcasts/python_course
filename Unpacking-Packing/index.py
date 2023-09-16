"""
 Unpacking Arguments
"""
# def institue(name, age, course):
#     print(name, age, course)

# mylist = {"name":"querycode", "age":10,"course":"python" }
# institue(**mylist)

# ============================================

"""
Packing Argument
"""

# def show(*args):
#     print(type(args))
#     print(*args)
# mytuple = (1,2,3)
# show(mytuple)
# ==================================
def packages(firstname = None, **kwargs):
    # print(type(kwargs))
    print(f"hello {firstname}")
    print(kwargs)

packages(name = "querycode.ir", age=10, course ="python")






"""
نکات کلیدی
# Packing Argument
امکان ارسال تعداد نامحدودی آرگومان به تابع را فراهم می‌کند.

#Unpacking Arguments
متغیری که آرگومان‌های بسته‌بندی شده در آن قرار دارند را به آرگومان‌های جداگانه تبدیل می‌کند.

 باعث کاهش کد و افزایش خوانایی و کارایی برنامه می‌ش
"""