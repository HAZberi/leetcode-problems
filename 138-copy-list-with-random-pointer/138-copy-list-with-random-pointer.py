from typing import List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None : None } #if we try to access a (Null/End of list) we always get None. 

        cur = head
        while cur:
            copy = Node(cur.val) #True copy
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]

#Test Cases
mySolution = Solution()

#Populate the Linklist

class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = Node(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

def listToArray(head: Optional[Node]):
    res = []
    nodeToIndex = {}

    cur = head
    i = 0
    while cur:
        nodeToIndex[cur] = i
        i += 1
        cur = cur.next

    curr = head
    while curr:
        if not curr.random:
            res.append([curr.val, None])
        else:
            res.append([curr.val, nodeToIndex[curr.random]])
        curr = curr.next
    
    return res

def populateFromArray(list: List) -> Optional[Node]:
    linklist = LinkedList()
    for val, _ in list:
        linklist.insertEnd(val)
    if linklist.head.next:
        linklist.head = linklist.head.next
    else:
        linklist.head = None
    
    cur = linklist.head
    i = 0
    while i < len(list):
        random = list[i][1]

        if random == None:
            cur.random = None
        else:
            locate = 0
            curr = linklist.head
            while random and locate < random:
                locate += 1
                curr = curr.next
            cur.random = curr

        cur = cur.next
        i += 1

    return linklist.head

print("Test Case 1: ", listToArray(mySolution.copyRandomList(populateFromArray([[7,None],[13,0],[11,4],[10,2],[1,0]]))))
print("Test Case 2: ", listToArray(mySolution.copyRandomList(populateFromArray([[1,1],[2,1]]))))
print("Test Case 3: ", listToArray(mySolution.copyRandomList(populateFromArray([[3,None],[3,0],[3,None]]))))

