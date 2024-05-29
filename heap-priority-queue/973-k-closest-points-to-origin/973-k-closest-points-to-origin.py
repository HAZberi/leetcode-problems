from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res

#Test Cases 
mySolution = Solution()
print("Test Case 1: ", mySolution.kClosest([[1,3],[-2,2]], 1))
print("Test Case 2: ", mySolution.kClosest([[3,3],[5,-1],[-2,4]], 2))
