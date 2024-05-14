from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#Test Cases
mySolution = Solution()

#Populate the Linklist

class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

def populateFromArray(list: List) -> Optional[ListNode]:
    linklist = LinkedList()
    for el in list:
        linklist.insertEnd(el)
    if linklist.head.next:
        linklist.head = linklist.head.next
    else:
        linklist.head = None
    return linklist.head

def makeCycle(list: List, pos: int) -> Optional[ListNode]:
    head = populateFromArray(list)

    indexToNode = {}
    i = 0
    cur = head
    while cur:
        indexToNode[i] = cur
        cur = cur.next
        i += 1
    
    tail = head
    while tail.next:
        tail = tail.next
    
    if pos > -1:
        tail.next = indexToNode[pos]
    
    return head

print("Test Case 1: ", mySolution.hasCycle(makeCycle([3,2,0,-4], 1)))
print("Test Case 2: ", mySolution.hasCycle(makeCycle([1,2], 0)))
print("Test Case 3: ", mySolution.hasCycle(makeCycle([1], -1)))