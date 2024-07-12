from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        second_last_loot, last_loot = 0, 0

        for current_house in nums:
            loot = max(current_house + second_last_loot, last_loot)
            second_last_loot = last_loot
            last_loot = loot
        
        return last_loot

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.rob([2,3,2]))
print("Test Case 2: ", my_solution.rob([1,2,3,1]))
print("Test Case 3: ", my_solution.rob([1,2,3]))
