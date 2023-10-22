# class Base:
#     a: int = 3
#     b: str = 'abc'

# class Derived(Base):
#     print(Base.__annotations__)

# Derived
# # ===============================
# from __future__ import annotations
# def foo(a: str): 
#     pass

# print(foo.__annotations__)
# # ===========================
from typing import Tuple

def foo(x: int) -> Tuple[str]:
    result = (str(x),)
    print("hello", type(result))
    return result

foo(1)
################################