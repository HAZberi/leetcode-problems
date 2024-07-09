from typing import List


class DFSSolution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = { i:[] for i in range(len(edges) + 1) }
        
        visited = set()
        def dfs(source, target):
            if source == target:
                return True
            visited.add(source)
            for neigbour in adj[source]:
                if neigbour not in visited and dfs(neigbour, target):
                    visited.remove(source)
                    return True
            visited.remove(source)
            return False

        for n1, n2 in edges:
            if dfs(n1, n2):
                return [n1, n2]
            
            adj[n1].append(n2)
            adj[n2].append(n1)

#Test Case
my_dfs_solution = DFSSolution()
print("Test Case 1: ", my_dfs_solution.findRedundantConnection([[1,2],[1,3],[2,3]]))
print("Test Case 2: ", my_dfs_solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
