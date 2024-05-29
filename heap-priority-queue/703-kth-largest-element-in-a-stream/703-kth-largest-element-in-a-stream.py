import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

#Test Cases
mySolution = KthLargest(3, [4, 5, 8, 2])
print(mySolution.add(3))
print(mySolution.add(5))
print(mySolution.add(10))
print(mySolution.add(9))
print(mySolution.add(4))
    