from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Building and adjacency list
        prereqMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        
        output = [] #Resultant list 
        visited = set() #keep track of courses that can be completed
        cycle = set() #keep track of courses along the current DFS path. Help in detecting cycle

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in prereqMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return output

#Test Case
mySolution = Solution()
print("Test Case 1: ", mySolution.findOrder(2, [[1,0]]))
print("Test Case 2: ", mySolution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print("Test Case 3: ", mySolution.findOrder(1, []))

