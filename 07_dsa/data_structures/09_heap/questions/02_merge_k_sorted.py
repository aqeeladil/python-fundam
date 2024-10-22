

# Merge K Sorted Lists

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    min_heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i))
    
    dummy = ListNode()
    current = dummy
    while min_heap:
        val, idx = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(min_heap, (lists[idx].val, idx))
    
    return dummy.next


