class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None   # empty LL
        self.n = 0


    def __len__(self):
        return self.n
    

    def insert_head(self, value):

        new_node = Node(value)      # new node
        new_node.next = self.head     # create connection
        self.head = new_node           # reassign head
        self.n += 1                      # increment n

    
    def __str__(self):
        curr = self.head
        result = ''

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    

    def append(self, value):

        new_node = Node(value)

        if self.head == None:
            # empty
            self.head = new_node
            self.n += 1
            return 

        curr = self.head
         
        while curr.next != None:
            curr = curr.next
        # you are at the last node  
        curr.next = new_node
        self.n += 1


    def insert_middle(self, after, value):

        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not found'
        
    
    def clear(self):
        self.head = None
        self.n = 0
    

    def delete_head(self):

        if self.head == None:
            return 'Empty LL'
        
        self.head = self.head.next
        self.n -= 1

    
    def pop(self):

        if self.head == None:
            return 'Empty LL'
        
        curr = self.head

        if curr.next == None:
            # single node
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next

        # at second last node
        curr.next = None
        self.n -= 1


    def remove(self, value):

        if self.head == None:
            return 'Empty LL'
        
        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        if curr.next == None:
            return 'Item not found'
        else:
            curr.next = curr.next.next
            self.n -= 1

    
    def find(self, value):

        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == value:
                return f"Item {value} at index {pos}"
            curr = curr.next
            pos += 1

        return 'Not found'


    def __getitem__(self,index):
        
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return f"Item {curr.data} at index {index}"
            curr = curr.next
            pos = pos + 1

        return 'IndexError'     
        



L = Linkedlist()
L.insert_head(6)
L.insert_head(5)
L.insert_head(4)
L.insert_head(3)
print(L)

L.append(99)
print(L)

L.insert_middle(5, 77)
print(L)

L.delete_head()
L.pop()
print(L)

L.remove(5)
print(L)

print(L.find(77))
# print(L.__getitem__(2))
print(L[2])




    


    


