from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            #Take the values from the lists
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10 #unit's place
            cur.next = ListNode(val)

            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

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
        
print("Test Case 1: ", listToArray(mySolution.addTwoNumbers(populateFromArray([2,4,3]), populateFromArray([5,6,4]))))
print("Test Case 2: ", listToArray(mySolution.addTwoNumbers(populateFromArray([0]), populateFromArray([0]))))
print("Test Case 3: ", listToArray(mySolution.addTwoNumbers(populateFromArray([9,9,9,9,9,9,9]), populateFromArray([9,9,9,9]))))
