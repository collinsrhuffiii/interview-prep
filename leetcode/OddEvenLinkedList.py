'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        head_odd = head
        head_even = head.next
        if not head_even:
            return head_odd
        cur_odd = head_odd
        cur_even = head_even
        while(cur_even and cur_even.next):
            cur_odd.next = cur_even.next
            cur_even.next = cur_odd.next.next
            cur_odd = cur_odd.next
            cur_even = cur_even.next
        cur_odd.next = head_even

        return head_odd

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
sol = Solution()
print('Input')
cur = head
while cur:
    print(str(cur.val)+ '->', end='')
    cur = cur.next
print('None')
print('Output')
cur = sol.oddEvenList(head)
while cur:
    print(str(cur.val)+ '->', end='')
    cur = cur.next
print('None')
print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
sol = Solution()
print('Input')
cur = head
while cur:
    print(str(cur.val)+ '->', end='')
    cur = cur.next
print('None')
print('Output')
cur = sol.oddEvenList(head)
while cur:
    print(str(cur.val)+ '->', end='')
    cur = cur.next
print('None')
print()
