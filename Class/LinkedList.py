class N:
    def __init__(self, *args):
        self.data = {}
        for i in args:
            self.append(i)

    def append(self, value):
        self.data[len(self.data)] = value

    def __str__(self):
        return f"{self.data.values()}"
    
    def __getitem__(self, index):
        return f"{self.data[index]}"
    
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __iter__(self):
        return iter(self.data)

    def __delitem__(self, index):
        del (self.data[index])

n = N('salam')
n.append("siyamak1")
del n[0]
n.append("siyamak2")
n.append("siyamak3")
n[0] = "amir"
print(n)
print(50*'@')
for num in n:
    print(num)
print(50 * "*")
print(n)
