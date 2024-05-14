from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class RecursiveDFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root:
            queue.append(root)
        
        depth = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth += 1
        
        return depth

class IterativeDFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
        
        return res

def insert(root: TreeNode, val:int, visited):
    if not root:
        root = TreeNode(val) if val else None
        return 
    
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        curr = queue.popleft()
        if not curr.left and curr not in visited:
            curr.left = TreeNode(val) if val else None
            if not curr.left:
                visited[curr] = [-1, -1]
                visited[curr][0] = 0
            break
        elif not curr.left and curr in visited and visited[curr][0] != 0:
            curr.left = TreeNode(val) if val else None
            if not curr.left:
                visited[curr][0] = 0 
            break
        elif not curr.left and visited[curr][0] == 0:
            visited[curr][0] = 0
        else:
            queue.append(curr.left)
        if not curr.right and curr not in visited:
            curr.right = TreeNode(val) if val else None
            if not curr.right:
                visited[curr] = [-1, -1]
                visited[curr][1] = 1
            break
        elif not curr.right and curr in visited and visited[curr][1] != 1:
            curr.right = TreeNode(val) if val else None
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
#Test Cases
myRDFS = RecursiveDFSSolution()
myBFS = BFSSolution()
myIDFS = IterativeDFSSolution()

testCase1 = populateTree([3,9,20,None,None,15,7])
print("Test Case 1: ", myRDFS.maxDepth(testCase1))
print("Test Case 1: ", myBFS.maxDepth(testCase1))
print("Test Case 1: ", myIDFS.maxDepth(testCase1))
testCase2 = populateTree([1,None,2])
print("Test Case 2: ", myRDFS.maxDepth(testCase2))
print("Test Case 2: ", myBFS.maxDepth(testCase2))
print("Test Case 2: ", myIDFS.maxDepth(testCase2))