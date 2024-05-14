from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next

    def getKth(self, curr: Optional[ListNode], k: int):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    

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


print("Test Case 1:", listToArray(mySolution.reverseKGroup(populateFromArray([1,2,3,4,5]), 2)))
print("Test Case 2:", listToArray(mySolution.reverseKGroup(populateFromArray([1,2,3,4,5]), 3)))
print("Test Case 3:", listToArray(mySolution.reverseKGroup(populateFromArray([1,2,3,4,5,7,8,9,10]), 4)))