import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i:i[0])
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1 
        
        return [res[q] for q in queries]
    
#Test Case 
mysolution = Solution()
print("Test Case 1: ", mysolution.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))
print("Test Case 2: ", mysolution.minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))

