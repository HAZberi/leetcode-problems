from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in neighbors:
                    r, c = dr + row, dc + col
                    if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1 

#Test Cases
mySolution = Solution()
print("Test Case 1: ", mySolution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print("Test Case 2: ", mySolution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print("Test Case 3: ", mySolution.orangesRotting([[0,2]]))

