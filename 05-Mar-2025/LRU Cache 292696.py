# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary for O(1) access
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail  # Link head to tail
        self.tail.prev = self.head  # Link tail to head

    # Move node to the front (most recently used)
    def _move_to_front(self, node):
        self._remove(node)
        self._add(node)

    # Remove node from list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Add node next to head (most recently used)
    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)  # Mark as recently used
            return node.value
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove LRU (tail's previous node)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)
