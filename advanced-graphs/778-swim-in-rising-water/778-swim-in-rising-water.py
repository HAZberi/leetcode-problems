import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) #n x n grid
        minHeap = [(0, 0, 0)] #(maxTime/maxHeight, r, c)
        visited = set((0, 0))

        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in neighbours:
                neiR, neiC = dr + r, dc + c
                if min(neiR, neiC) < 0 or max(neiR, neiC) >= N or (neiR, neiC) in visited:
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minHeap, (max(t, grid[neiR][neiC]), neiR, neiC))

#Test Case 
my_solution = Solution()
print("Test Case 1: ", my_solution.swimInWater([[0,2],[1,3]]))
print("Test Case 2: ", my_solution.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))


