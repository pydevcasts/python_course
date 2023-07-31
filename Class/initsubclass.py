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