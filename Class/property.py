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