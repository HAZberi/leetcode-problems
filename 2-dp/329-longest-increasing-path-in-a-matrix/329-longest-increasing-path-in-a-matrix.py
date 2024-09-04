from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} #(row, col): increasing-length 

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            
            neigbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in neigbours:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            
            dp[(r, c)] = res
            return dp[(r, c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        
        return max(dp.values())
    

#Test Cases
mysolution = Solution()
print("Test Case 1: ", mysolution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print("Test Case 2: ", mysolution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print("Test Case 3: ", mysolution.longestIncreasingPath([[1]]))
