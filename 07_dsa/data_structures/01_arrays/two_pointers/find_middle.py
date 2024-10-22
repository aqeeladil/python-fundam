# Given a singly linked list, find the middle element. 
# If there are two middle elements, return the second one.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val



# Time Complexity: O(n), where n is the number of nodes in the linked list.


