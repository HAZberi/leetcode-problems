from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or min(r, c) < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS - 1, c, atlantic, 0)
        
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS - 1, atlantic, 0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res

#Test Cases
mySolution = Solution()
print("Test Case 1", mySolution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print("Test Case 2", mySolution.pacificAtlantic([[1]]))
        
