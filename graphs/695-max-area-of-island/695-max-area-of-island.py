from typing import List


class DFSSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            area = 1
            area += dfs(r + 1, c) 
            area += dfs(r - 1, c) 
            area += dfs(r, c + 1) 
            area += dfs(r, c - 1)

            return area

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(dfs(r, c), maxArea)

        return maxArea 

#Test Cases
myDFSSolution = DFSSolution()
print("Test Case 1: ", myDFSSolution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print("Test Case 2: ", myDFSSolution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
