from collections import deque
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

class BFSSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            area = 1

            neighbours = [[0, 1],[0, -1],[1, 0],[-1, 0]]

            while queue:
                row, col = queue.popleft()
                for dr, dc in neighbours:
                    r, c = dr + row, dc + col
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1:
                        queue.append((r, c))
                        visited.add((r, c))
                        area += 1
            
            return area

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(bfs(r, c), maxArea)
        
        return maxArea

#Test Cases
myBFSSolution = BFSSolution()
print("Test Case 1: ", myBFSSolution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print("Test Case 2: ", myBFSSolution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
