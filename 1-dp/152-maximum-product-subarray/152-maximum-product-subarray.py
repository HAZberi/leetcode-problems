from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue

            temp = curMax #old curMax
            curMax = max(curMax * n, curMin * n, n) #new curMax
            curMin = min(temp, curMin * n, n) #new curMin needs old curMax

            res = max(res, curMax)
        
        return res

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.maxProduct([2,3,-2,4]))
print("Test Case 2: ", my_solution.maxProduct([-2,0,-1]))

