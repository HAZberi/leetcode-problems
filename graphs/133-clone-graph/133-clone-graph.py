
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import List, Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node) if node else None

#Test Cases
def graphSize(adj_list: List) -> int:
    return len(adj_list)

def make_graph(adj_list: List) -> Node:
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0]

def make_list(node: Node, size: int) -> List:
    if not Node:
        return []
    list = [0] * size
    while size > 0 and node:
        if list[node.val - 1] != 0:
            node = node.neighbors.pop() if node.neighbors else None
            continue

        list[node.val - 1] = [neighbour.val for neighbour in node.neighbors] if node.neighbors else []
        node = node.neighbors.pop() if node.neighbors else None 
        size -= 1
    
    return list
            

mySolution = Solution()
print("Test Case 1: ", make_list(mySolution.cloneGraph(make_graph([[2,4],[1,3],[2,4],[1,3]])), graphSize([[2,4],[1,3],[2,4],[1,3]])))
print("Test Case 2: ", make_list(mySolution.cloneGraph(make_graph([[]])), graphSize([[]])))
print("Test Case 3: ", make_list(mySolution.cloneGraph(make_graph([])), graphSize([])))
print("Test Case 4: ", make_list(mySolution.cloneGraph(make_graph([[2],[1,3],[2]])), graphSize([[2],[1,3],[2]])))
