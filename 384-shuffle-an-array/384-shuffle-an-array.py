from random import randint
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)-1, 0, -1):
            randomIndex = randint(0, i)

            self.nums[i], self.nums[randomIndex] = self.nums[randomIndex], self.nums[i]

        return self.nums

#Test Cases

mySolution = Solution([1,2,3])

print("Shuffle", mySolution.shuffle())
print("Reset", mySolution.reset())
print("Shuffle", mySolution.shuffle())
print("Reset", mySolution.reset())