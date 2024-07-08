from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n

        def find(node):
            res = node
            while res != parent[node]:
                parent[node] = parent[parent[node]] #This path compression by 2 level. 
                res = parent[node] #Setting grandparent
            return res
        
        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)

            if parent1 == parent2:
                return 0
            
            if size[parent1] < size[parent2]:
                parent[parent1] = parent2
                size[parent2] += size[parent1]
            else:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            return 1
        
        num_of_components = n 
        for n1, n2 in edges:
            num_of_components -= union(n1, n2)
        
        return num_of_components

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.countComponents(3, [[0,1], [0,2]]))
print("Test Case 2: ", my_solution.countComponents(6, [[0,1], [1,2], [2,3], [4,5]]))
