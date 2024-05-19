from collections import deque
from typing import List, Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)            
            dfs(root.right)

        dfs(root)
        return ",".join(res)            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

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

#Test Cases:
mySolution = Codec()

print("Test Case 1 Serialize:", mySolution.serialize(populateTree([1,2,3,None,None,4,5])))
print("Test Case 1 Deserialize:", printTreeAsList(mySolution.deserialize(mySolution.serialize(populateTree([1,2,3,None,None,4,5])))))
print("Test Case 2 Serialize:", mySolution.serialize(populateTree([])))
print("Test Case 2 Deserialize:", printTreeAsList(mySolution.deserialize(mySolution.serialize(populateTree([])))))