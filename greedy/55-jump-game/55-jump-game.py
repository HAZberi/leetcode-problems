from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= goal:
                goal = i

        return goal == 0

#Test Case:
my_solution = Solution()
print("Test Case 1: ", my_solution.canJump([2,3,1,1,4]))
print("Test Case 2: ", my_solution.canJump([3,2,1,0,4]))
