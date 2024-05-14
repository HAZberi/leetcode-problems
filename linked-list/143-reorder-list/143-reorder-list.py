from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next #second portion of the list
        prev = slow.next = None

        #Reverse the second portion
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        #Merge the two portions of the list
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


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

t1 = populateFromArray([1,2,3,4])
t2 = populateFromArray([1,2,3,4,5])

mySolution.reorderList(t1)
mySolution.reorderList(t2)

print("Test Case 1: ", listToArray(t1))
print("Test Case 2: ", listToArray(t2))
