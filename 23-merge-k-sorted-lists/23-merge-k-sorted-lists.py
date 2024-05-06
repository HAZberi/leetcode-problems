from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedlists.append(self.mergeTwoLists(l1, l2))
            lists = mergedlists
        
        return lists[0]
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode(-1)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        
        return dummy.next

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

def listOflists(lists: List[List]) -> List[Optional[ListNode]]:
    res = []
    for i in range(len(lists)):
        res.append(populateFromArray(lists[i]))
    return res

print("Test Case 1: ", listToArray(mySolution.mergeKLists(listOflists([[1,4,5],[1,3,4],[2,6]]))))
print("Test Case 2: ", listToArray(mySolution.mergeKLists(listOflists([]))))
print("Test Case 3: ", listToArray(mySolution.mergeKLists(listOflists([[]]))))