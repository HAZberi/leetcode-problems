import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Total number of points/nodes
        N = len(points)

        #Building the adjacency list
        adj = { i:[] for i in range(N) }
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        #Prims's Algorithm
        #Setup
        visited = set()
        res = 0 #total cost of MST
        minHeap = [(0,0)] #(cost, point)

        #Running Prims
        while len(visited) < N:
            cost, dest = heapq.heappop(minHeap)
            if dest in visited:
                continue

            res += cost
            visited.add(dest)

            for neiCost, nei in adj[dest]:
                heapq.heappush(minHeap, (neiCost, nei))
        
        return res


#Test Case
my_solution = Solution()
print("Test Case 1: ", my_solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print("Test Case 2: ", my_solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))

