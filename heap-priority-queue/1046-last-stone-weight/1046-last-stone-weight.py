from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, abs(y - x))
        
        stones.append(0)
        return abs(stones[0])

#Test Cases
mySolution = Solution()

print("Test Case 1: ", mySolution.lastStoneWeight([2,7,4,1,8,1]))
print("Test Case 2: ", mySolution.lastStoneWeight([1]))
