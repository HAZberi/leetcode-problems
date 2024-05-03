from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

class RecursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head #Reversing next pointers
        
        head.next = None

        return newhead

#Test Cases
mySolution = Solution()
mySolutionR = RecursiveSolution()

#Populate the Linklist

class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

def listToArray(head: Optional[ListNode]):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    
    return res

def populateFromArray(list: List) -> Optional[ListNode]:
    linklist = LinkedList()
    for el in list:
        linklist.insertEnd(el)
    if linklist.head.next:
        linklist.head = linklist.head.next
    else:
        linklist.head = None
    return linklist.head


print("Test Case 1: ", listToArray(mySolution.reverseList(populateFromArray([1,2,3,4,5]))))
print("Test CaseR 1: ", listToArray(mySolutionR.reverseList(populateFromArray([1,2,3,4,5]))))
print("Test Case 2: ", listToArray(mySolution.reverseList(populateFromArray([1,2]))))
print("Test CaseR 2: ", listToArray(mySolutionR.reverseList(populateFromArray([1,2]))))
print("Test Case 3: ", listToArray(mySolution.reverseList(populateFromArray([]))))
print("Test CaseR 3: ", listToArray(mySolutionR.reverseList(populateFromArray([]))))
