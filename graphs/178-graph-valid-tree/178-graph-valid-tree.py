from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        #Make adjacency list
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for neighbour in adj[curr]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, curr):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visited)

#Test Cases
mySolution = Solution()
print("Test Case 1: ", mySolution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print("Test Case 2: ", mySolution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
