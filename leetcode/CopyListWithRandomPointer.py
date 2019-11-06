'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        old_new_map = {}
        new_head = RandomListNode(head.label)
        new_cur = new_head
        old_cur = head
        while old_cur:
            old_new_map[old_cur] = new_cur
            if old_cur.next:
                new_cur.next = RandomListNode(old_cur.next.label)
            new_cur = new_cur.next
            old_cur = old_cur.next

        new_cur = new_head
        old_cur = head
        while old_cur:
            if old_cur.random:
                new_cur.random = old_new_map[old_cur.random]
            old_cur = old_cur.next
            new_cur = new_cur.next

        return new_head


head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
head.next.next.next = RandomListNode(4)
head.next.next.next.next = RandomListNode(5)

head.random = head.next.next
head.next.next.random = head.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

sol = Solution()
cur = head
print('Input')
print('next')
while cur:
    print(str(cur.label) + '->', end='')
    cur = cur.next
print('None')
print()
print('random')
cur = head
while cur:
    if cur.random:
        print(str(cur.label) + '->' + str(cur.random.label))
    else:
        print(str(cur.label) + '->None')
    cur = cur.next
print()

copy = sol.copyRandomList(head)
print('Output')
print('next')
cur = copy
while cur:
    print(str(cur.label) + '->', end='')
    cur = cur.next
print('None')
print()
print('random')
cur = copy
while cur:
    if cur.random:
        print(str(cur.label) + '->' + str(cur.random.label))
    else:
        print(str(cur.label) + '->None')
    cur = cur.next
print()

head = RandomListNode(-1)
head.random = head

sol = Solution()
cur = head
print('Input')
print('next')
while cur:
    print(str(cur.label) + '->', end='')
    cur = cur.next
print('None')
print()
print('random')
cur = head
while cur:
    if cur.random:
        print(str(cur.label) + '->' + str(cur.random.label))
    else:
        print(str(cur.label) + '->None')
    cur = cur.next
print()

copy = sol.copyRandomList(head)
print('Output')
print('next')
cur = copy
while cur:
    print(str(cur.label) + '->', end='')
    cur = cur.next
print('None')
print()
print('random')
cur = copy
while cur:
    if cur.random:
        print(str(cur.label) + '->' + str(cur.random.label))
    else:
        print(str(cur.label) + '->None')
    cur = cur.next
print()
