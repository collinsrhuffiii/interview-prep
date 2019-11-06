'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        cur_node = head
        carry = 0
        while(l1 != None or l2 != None):
            if l1 == None:
                l1_num = 0
            else: 
                l1_num = l1.val
                l1 = l1.next
            if l2 == None:
                l2_num = 0
            else: 
                l2_num = l2.val
                l2 = l2.next

            cur_node.next = ListNode((l1_num+l2_num+carry) % 10)
            carry = (l1_num +l2_num + carry) // 10
            cur_node = cur_node.next
        if carry > 0:
            cur_node.next = ListNode(carry)
        return head.next

        '''
        Original Solution
        num1 = 0
        i = 0
        while(l1 != None):
            num1 = num1 + l1.val * (10**i)
            i+=1
            l1 = l1.next

        num2 = 0
        i = 0
        while(l2 != None):
            num2 = num2 + l2.val * (10**i)
            i+=1
            l2 = l2.next
        
        sum_nums = num1 + num2
        output = ListNode(sum_nums % 10)
        cur_node = output
        i = 1
        while(sum_nums > (10**i-1)):
            cur_node.next = ListNode(sum_nums // 10**i % 10)
            cur_node = cur_node.next
            i += 1
        return output
        '''


ll1 = ListNode(2)
ll1.next = ListNode(4)
ll1.next.next = ListNode(3)
ll2 = ListNode(5)
ll2.next = ListNode(6)
ll2.next.next = ListNode(4)
sol = Solution()
out = sol.addTwoNumbers(ll1, ll2)
while(out != None):
    print(out.val)
    out = out.next
