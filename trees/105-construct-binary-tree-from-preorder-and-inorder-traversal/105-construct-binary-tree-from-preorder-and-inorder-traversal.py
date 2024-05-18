from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

def printTreeAsList(root: TreeNode) -> List:
    result = []
    queue = deque()

    if root:
        queue.append(root)
    
    while len(queue) > 0:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == "null":
                result.append("null")
            if curr != "null":
                result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                else:
                    queue.append("null")
                if curr.right:
                    queue.append(curr.right)
                else:
                    queue.append("null")

    for i in range(len(result) - 1, -1, -1):
        if result[i] != "null":
            return result
        result.pop()

#Test Cases
mySolution = Solution()
print("Test Case 1: ", printTreeAsList(mySolution.buildTree([3,9,20,15,7], [9,3,15,20,7])))
print("Test Case 1: ", printTreeAsList(mySolution.buildTree([4,5,3,17,2,6,7,1,9,8,10,11,13,14,15,20,19], [3,2,6,17,1,7,5,9,8,4,10,14,13,11,20,15,19])))
print("Test Case 2: ", printTreeAsList(mySolution.buildTree([-1],[-1])))
