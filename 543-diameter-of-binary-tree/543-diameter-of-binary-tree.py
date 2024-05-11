from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            diameter[0] = max(diameter[0], (2 + left + right))

            return 1 + max(left, right)

        dfs(root)
        return diameter[0]

def insert(root: TreeNode, val:int):
    
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        curr = queue.popleft()
        if not curr.left:
            curr.left = TreeNode(val) if val else None
            break
        else:
            queue.append(curr.left)

        if not curr.right:
            curr.right = TreeNode(val) if val else None
            break
        else:
            queue.append(curr.right)

def populateTree(list: List) -> TreeNode:
    if len(list) < 1:
        return None
    
    root = TreeNode(list[0])
    for i in range(1, len(list)):
        insert(root, list[i])
    
    return root

#Test Cases:
mySolution = Solution()
testCase1 = populateTree([1,2,3,4,5])
print("Test Case 1: ", mySolution.diameterOfBinaryTree(testCase1))
print("Test Case 2: ", mySolution.diameterOfBinaryTree(populateTree([1,2])))
    

    