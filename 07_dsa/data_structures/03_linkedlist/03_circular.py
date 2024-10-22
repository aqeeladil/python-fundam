# Circular lists are useful for applications where the list needs to 
# be cycled through continuously.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def traverse(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    def delete_node(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
                return
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = temp.next
            return
        temp = self.head
        prev = None
        while temp.data != key:
            if temp.next == self.head:
                return
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None
