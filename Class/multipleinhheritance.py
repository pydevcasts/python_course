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