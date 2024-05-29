from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = [0]
        self.k = k
        for n in nums:
            self.push(n)

    def add(self, val: int) -> int:
        self.push(val)
        return self.maxHeap[self.k]
    
    def push(self, val: int):
        self.maxHeap.append(val)
        i = len(self.maxHeap) - 1

        #percolate up
        while self.maxHeap[i] > self.maxHeap[i // 2]:
            temp = self.maxHeap[i]
            self.maxHeap[i] = self.maxHeap[i // 2]
            self.maxHeap[i // 2] = temp
            i = i // 2
    