import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = { i:[] for i in range(1, n + 1) }
        for u, v, w in times:
            adj[u].append((v, w))
        
        visited = set()
        resTotal = 0
        minHeap = [(0, k)]

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            resTotal = max(resTotal, t1)

            for neighbour, time in adj[n1]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (t1 + time, neighbour))
        
        return resTotal if len(visited) == n else -1

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print("Test Case 2: ", my_solution.networkDelayTime([[1,2,1]], 2, 1))
print("Test Case 3: ", my_solution.networkDelayTime([[1,2,1]], 2, 2))
