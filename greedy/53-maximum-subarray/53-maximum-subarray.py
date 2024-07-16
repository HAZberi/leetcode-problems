from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += n
            maxSum = max(curSum, maxSum)
        
        return maxSum

#Test Case
my_solution = Solution()
print("Test Case 1: ", my_solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print("Test Case 2: ", my_solution.maxSubArray([1]))
print("Test Case 3: ", my_solution.maxSubArray([5,4,-1,7,8]))

