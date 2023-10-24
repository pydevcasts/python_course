"""
    __init_subclass__
"""

# class A:
#     def __init_subclass__(cls) -> None:
#         print(cls)
#         print("class A is subclassed")

# class B(A):
#     pass

# class C(A):
#     pass
# ==============================
# class Parent:
#     def __init_subclass__(cls):
#         print(f'Subclass of Parent Created!{cls}')

# class Child(Parent):
#     pass

# class Grandchild(Child):
#     pass
########################################
# class A:
#     @classmethod
#     def __init_subclass__(cls) -> None:
#         print("class A is subclassed")

# class B(A):
#     @classmethod
#     def __init_subclass__(cls) -> None:
#         print("class B is subclassed")


# class C(B):
#     pass
# ==================================
# class A:
#     @classmethod
#     def __init_subclass__(cls, name) -> None:
#         print(f"class A is subclassed and it name is:{name}")

# class B(A, name = "siyamak"):
#     pass
##########################################
class A:
    def __init_subclass__(cls,**kwargs) -> None:
        super.__init_subclass__(**kwargs)
        cls.x = "daee doset dare"

class B(A):
    x = "diyana"

b=B()
print(b.x)