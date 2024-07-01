from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Make an ajacency list map from the given edges
        prereqMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        
        #Using a hashset in order to keep track of visited courses along the current DFS path
        visited = set()

        #Recursive DFS 
        def dfs(crs):
            if crs in visited: #Cycle Detection
                return False
            
            if prereqMap[crs] == []: #Course can be completed
                return True

            visited.add(crs)
            for pre in prereqMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prereqMap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

#Test Cases
mySolution = Solution()
print("Test Case 1: ", mySolution.canFinish(2, [[1,0]]))
print("Test Case 2: ", mySolution.canFinish(2, [[1,0],[0,1]]))

