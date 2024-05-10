from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
def insert(root: TreeNode, val:int):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    
    return root

def populateTree(list: List) -> Optional[TreeNode]:
    if len(list) < 1:
        return None
    
    root = TreeNode(list[0])
    for i in range(1, len(list)):
        insert(root, list[i])
    
    return root

def preorderDFS(root: TreeNode, result: List):
    if not root:
        return None

    result.append(root.val)
    preorderDFS(root.left, result)
    preorderDFS(root.right, result)

    return root

def printTreeAsDFS(root:TreeNode):
    result = []
    preorderDFS(root, result)
    return result

def printTreeAsList(root: TreeNode) -> List:
    result = []
    queue = deque()

    if root:
        queue.append(root)
    
    while len(queue) > 0:
        for i in range(len(queue)):
            curr = queue.popleft()
            result.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return result

#Test Cases
mySolution = Solution()

testCase1 = populateTree([4,2,7,1,3,6,9])
print("Test Case 1: ", printTreeAsList(mySolution.invertTree(testCase1)))
# print("Test Case 1: ", printTreeAsDFS(mySolution.invertTree(testCase1)))

testCase2 = populateTree([2,1,3])
testCase2Sol = mySolution.invertTree(testCase2)
print("Test Case 2: ", printTreeAsList(testCase2Sol))
# print("Test Case 2: ", printTreeAsDFS(mySolution.invertTree(testCase2)))

testCase3 = populateTree([])
print("Test Case 3: ", printTreeAsList(mySolution.invertTree(testCase3)))
