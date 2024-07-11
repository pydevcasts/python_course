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
########################################################################
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self, head: Node):
        self.head = head
    
    def to_string(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

node1 = Node(value=2)
node2 = Node(value='siyamak')
node3 = Node(value='sanaz')

node1.next = node2
node2.next = node3

ll = LinkedList(head=node1)
ll.to_string()
