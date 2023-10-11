class Singleton(type):
    _value = None
    def __call__(self, *args: any, **kwds: any) -> any:
        if self._value is None:
            self._value =  super().__call__(*args, **kwds)
        return self._value
    
class Main(metaclass=Singleton):
    pass

m = Main()
n = Main()
print(id(m))
print(id(n))