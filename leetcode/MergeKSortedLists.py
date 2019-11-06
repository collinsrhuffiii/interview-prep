'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        while(len(lists) > 1):
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            if l1 and l2:
                l = self.merge(l1, l2)
                lists.append(l)
            else:
                if l1:
                    lists.append(l1)
                if l2:
                    lists.append(l2)
        if lists:
            return lists[0]
        else:
            return None

    def merge(self, l1, l2):
        if l1.val > l2.val:
            l1, l2, = l2, l1

        head = l1
        while(l1.next != None and l2 != None):
            if l2.val >= l1.val and l2.val <= l1.next.val:
                temp1 = l1.next
                temp2 = l2.next
                l1.next = l2
                l2.next = temp1
                l2 = temp2
            else:
                l1 = l1.next
        if l2:
            l1.next = l2
        return head

sol = Solution()
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(5)

head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)

head3 = ListNode(7)
head3.next = ListNode(8)
head3.next.next = ListNode(9)

lists = [head1, head2, head3]
                 
ret_head = sol.mergeKLists(lists)
while(ret_head != None):
    print(ret_head.val)
    ret_head = ret_head.next
