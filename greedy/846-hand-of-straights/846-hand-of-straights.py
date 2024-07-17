import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            smallest = minHeap[0]
            for i in range(smallest, smallest + groupSize):
                if i not in count or count[i] < 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if minHeap[0] != i:
                        return False
                    heapq.heappop(minHeap)
        
        return True
    
#Test Case:
my_solution = Solution()
print("Test Case 1: ", my_solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print("Test Case 2: ", my_solution.isNStraightHand([1,2,3,4,5], 4))
print("Test Case 3: ", my_solution.isNStraightHand([1,1,3,6,2,3,4,7,8], 3))

