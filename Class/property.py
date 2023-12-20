class N:
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname
        self.email = f"{self.fname}_{self.lname}@gmail.com"

        
    @property
    def email(self):
        return f"{self.fname}_{self.lname}@gmail.com"
    
n = N("zahra", "riyahi")
n.fname = "fateme"
print(n.lname)
print(n.fname)
print(n.email)
###################################################
class Student:
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter   #property-name.setter decorator
    def name(self, value):
        self.__name = value

    @name.deleter   #property-name.deleter decorator
    def name(self):
        print('Deleting..')
        del self.__name

s = Student('Steve')
print(s.name)  #'Steve'

s.name = 'Bill'
print(s.name)  #'Bill'


del s.name
print(s.name)  #AttributeError
        