

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


a = Node(4)
b = Node(5)
c = Node(6)

print(a)
print(a.data)
print(a.next)

a.next = b
b.next = c

print(a.next)
print(b.next)
print(c.next)






