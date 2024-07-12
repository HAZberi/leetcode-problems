from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        second_last_loot, last_loot = 0, 0

        for current_house in nums:
            loot = max(second_last_loot + current_house, last_loot)
            second_last_loot = last_loot
            last_loot = loot
        
        return last_loot

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.rob([1,2,3,1]))
print("Test Case 2: ", my_solution.rob([2,7,9,3,1]))
