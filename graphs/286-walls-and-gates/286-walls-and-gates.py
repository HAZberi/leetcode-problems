from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        distance = 0
        neighbors = [[0, 1],[0, -1],[1, 0],[-1, 0]]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                rooms[row][col] = distance

                for dr, dc in neighbors:
                    r, c = dr + row, dc + col
                    if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or rooms[r][c] == -1:
                        continue
                    queue.append((r, c))
                    visited.add((r, c))

            distance += 1
        
        return rooms

#TEST CASES
mysolution = Solution()
print("Test Case 1", mysolution.wallsAndGates([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]))
print("Test Case 2", mysolution.wallsAndGates([
  [0,-1],
  [1,2]
]))
