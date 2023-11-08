class A:
    def __init__(self, name):
        print(name)

class C(A):
    def __init__(self, age):
        super().__init__(name = "siyamak")
        print(age)
c = C(25)
###############################################
# class Parent:
#   def __init__(self, txt):
#     self.message = txt

#   def printmessage(self):
#     print(self.message)

# class Child(Parent):
#   def __init__(self, txt):
#     super().__init__(txt)

# x = Child("Hello, and welcome!")

# x.printmessage()

##################################################
class A:
    name = "ahmad"
    def call(self, a = ''):
        print(f"class A {a}")

class B:
    name = "ali"
    def call(self,b = '', **kwargs):
        print(f"class B {b}")
        super().call(**kwargs)

class C(B, A):
    name = "saed"
    def call(self,c = '', **kwargs):
        print(f"class C {c}")
        super().call(**kwargs)



c = C()
c.call(c = 'saed', b = "ali", a = 'siyamak')
#######################################################
class A:
    def __init__(self, a = ''):
        print(f"class A {a}")

class B:
    def __init__(self,b = '', **kwargs):
        print(f"class B {b}")
        super().__init__(**kwargs)

class C(B, A):
    def __init__(self,c = '', **kwargs):
        print(f"class C {c}")
        super().__init__(**kwargs)



c = C(c = 'saed', b = "ali", a = 'siyamak')
