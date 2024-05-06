class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # mapping keys to nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = Node(key, value)
        self.cache[key] = newnode
        self.insert(newnode)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

#Test Cases
testCase1 = LRUCache(2)

print("LRUCache: ", testCase1)
print("Put (1,1)", testCase1.put(1,1))
print("Put (2,2)", testCase1.put(2,2))
print("Get 1", testCase1.get(1))
print("Put (3,3)", testCase1.put(3,3))
print("Get 2", testCase1.get(2))
print("Put (4,4)", testCase1.put(4,4))
print("Get 1", testCase1.get(1))
print("Get 3", testCase1.get(3))
print("Get 4", testCase1.get(4))
