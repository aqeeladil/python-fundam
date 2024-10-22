# A cycle in a linked list occurs when a node's next pointer points back to a previous node, 
# creating a loop.


# Floyd’s Cycle-Finding Algorithm (Tortoise and Hare Algorithm).

def detect_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

