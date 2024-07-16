from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            copyDp = set()
            for possibleSum in dp:
                if (possibleSum + nums[i]) == target:
                    return True
                copyDp.add(possibleSum)
                copyDp.add(possibleSum + nums[i])
            dp = copyDp
        
        return True if target in dp else False

#Test Case
my_solution = Solution()
print("Test Case 1: ", my_solution.canPartition([1,5,11,5]))
print("Test Case 2: ", my_solution.canPartition([1,2,3,5]))
