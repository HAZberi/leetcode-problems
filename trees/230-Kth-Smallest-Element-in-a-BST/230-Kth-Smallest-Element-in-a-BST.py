from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        curr = root
        stack = []

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                n += 1
                if n == k:
                    return curr.val
                curr = curr.right
        
def insert(root: TreeNode, val:int, visited):
    if not root:
        root = TreeNode(val) if val or val==0 else None
        return 
    
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        curr = queue.popleft()
        if not curr.left and curr not in visited:
            curr.left = TreeNode(val) if val or val==0 else None
            if not curr.left:
                visited[curr] = [-1, -1]
                visited[curr][0] = 0
            break
        elif not curr.left and curr in visited and visited[curr][0] != 0:
            curr.left = TreeNode(val) if val or val==0 else None
            if not curr.left:
                visited[curr][0] = 0 
            break
        elif not curr.left and visited[curr][0] == 0:
            visited[curr][0] = 0
        else:
            queue.append(curr.left)
        if not curr.right and curr not in visited:
            curr.right = TreeNode(val) if val or val==0 else None
            if not curr.right:
                visited[curr] = [-1, -1]
                visited[curr][1] = 1
            break
        elif not curr.right and curr in visited and visited[curr][1] != 1:
            curr.right = TreeNode(val) if val or val==0 else None
            if not curr.right:
                visited[curr][1] = 1
            break
        elif not curr.right and visited[curr][1] == 1:
            visited[curr][1] = 1
        else:
            queue.append(curr.right)
        
def populateTree(list: List) -> Optional[TreeNode]:
    if len(list) < 1:
        return None
    
    root = TreeNode(list[0])
    visited = {} #CurrentNode: [0 for left, 1 for right]
    for i in range(1, len(list)):
        insert(root, list[i], visited)
    
    return root

#Test Cases:
mySolution = Solution()
print("Test Case 1: ", mySolution.kthSmallest(populateTree([3,1,4,None,2]), 1))
print("Test Case 2: ", mySolution.kthSmallest(populateTree([5,3,6,2,4,None,None,1]), 3))
