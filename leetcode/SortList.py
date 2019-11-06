'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1

        while(l1.next != None and l2 != None):
            if l1.val <= l2.val and l1.next.val >= l2.val:
                temp = l2.next
                l2.next = l1.next
                l1.next = l2
                l2 = temp
                l1 = l1.next
            else:
                l1 = l1.next
        if l1.next == None and l2 != None:
            while(l2 != None):
                l1.next = l2
                l2 = l2.next
                l1 = l1.next
        return head

    def sortList(self, head):
        cur_node = head
        num_nodes = 0
        while(cur_node != None):
            cur_node = cur_node.next
            num_nodes += 1
        head = self.sort(head, num_nodes)
        return head

    def sort(self, head, num_nodes):
        if num_nodes <= 1:
            return head
        else:
            head1 = head
            head2 = head
            cur_node = head2
            head2 = head2.next
            i = 1
            while(i < num_nodes//2 and head2.next != None):
                i += 1
                head2 = head2.next
                cur_node = cur_node.next
            cur_node.next = None
            head1 = self.sort(head1, i)
            head2 = self.sort(head2, num_nodes-i)
            head = self.mergeTwoLists(head1, head2)
            cur_node = head
            return head

sol = Solution()

head = ListNode(4)
head.next = ListNode(3)
head.next.next = ListNode(2)

ret_head = sol.sortList(head)
print('Test')
while(ret_head != None):
    print(ret_head.val)
    ret_head = ret_head.next

