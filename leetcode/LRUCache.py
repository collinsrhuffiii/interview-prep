'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.num_elements = 0
        self.key_node_map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_node_map:
            return -1
        node = self.key_node_map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
        else:
            if self.num_elements == self.capacity:
                node_to_remove = self.tail.prev
                self.key_node_map.pop(node_to_remove.key)
                node_to_remove.prev.next = self.tail
                self.tail.prev = node_to_remove.prev
                self.num_elements -= 1

            new_node = Node(key, value)
            self.key_node_map[key] = new_node
            new_node.prev = self.head
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node
            self.num_elements += 1




cache = LRUCache(2)
print(f'cache.put(1, 1): {cache.put(1, 1)}')
print(f'cache.put(2, 2): {cache.put(2, 2)}')
print(f'cache.get(1): {cache.get(1)}')
print(f'cache.put(3, 3): {cache.put(3, 3)}')
print(f'cache.get(2): {cache.get(2)}')
print(f'cache.put(4, 4): {cache.put(4, 4)}')
print(f'cache.get(1): {cache.get(1)}')
print(f'cache.get(3): {cache.get(3)}')
print(f'cache.get(4): {cache.get(4)}')
