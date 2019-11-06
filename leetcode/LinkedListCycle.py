'''
Given a linked list, determine if it has a cycle in it
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        ptr1 = head
        ptr2 = head
        if head.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if ptr2:
            ptr2 = ptr2.next

        while(ptr1 and ptr2):
            if ptr1 == ptr2:
                return True
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if ptr2:
                ptr2 = ptr2.next
        return False

        
