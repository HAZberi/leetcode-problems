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

class UnionFindSolution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        #return False if and edge is redundant
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

#Test Case
my_unionfind_solution = UnionFindSolution()
print("Test Case 1: ", my_unionfind_solution.findRedundantConnection([[1,2],[1,3],[2,3]]))
print("Test Case 2: ", my_unionfind_solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
