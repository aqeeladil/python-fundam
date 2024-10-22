# Merging two sorted linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Iterative Approach:
def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
            curr = curr.next
    curr.next = l1 or l2
    return dummy.next

# Time O(n + m), 
# Space O(1) 



