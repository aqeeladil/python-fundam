
# Reversing a linked list involves changing the direction of the next pointers in a singly linked list. 
# This operation can be done iteratively or recursively.


# Iterative Approach:

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head

# Time: O(n) 
# Space O(1).





