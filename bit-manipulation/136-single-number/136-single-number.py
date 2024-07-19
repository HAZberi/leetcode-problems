from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 #0 is the neural value for XOR
        for n in nums:
            res = res ^ n
        return res

#Test Case
my_solution = Solution()
print("Test Case 1: ", my_solution.singleNumber([2,2,1]))
print("Test Case 1: ", my_solution.singleNumber([4,1,2,1,2]))
print("Test Case 3: ", my_solution.singleNumber([4,6,2,4,2]))



