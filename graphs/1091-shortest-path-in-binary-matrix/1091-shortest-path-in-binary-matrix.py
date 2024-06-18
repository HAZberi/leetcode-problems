from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque()
        visited = set()

        if grid[0][0] == 0: #We have to check whether the first cell is a valid path or not.
            queue.append((0,0))
            visited.add((0,0))

            length = 1
            neighbours = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if r == N - 1 and c == N - 1:
                        return length
                    
                    for dr, dc in neighbours:
                        if min(dr + r, dc + c) < 0 or max(dr + r, dc + c) >= N or (dr + r, dc + c) in visited or grid[dr + r][dc + c] == 1:
                            continue
                        queue.append((dr + r, dc + c))
                        visited.add((dr + r, dc + c))
                length += 1
        
        return -1


