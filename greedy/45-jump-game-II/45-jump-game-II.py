from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(i + nums[i], farthest)
            l = r + 1
            r = farthest
            res += 1
        
        return res

#Test Case 
my_solution = Solution()
print("Test case 1: ", my_solution.jump([2,3,1,1,4]))
print("Test case 1: ", my_solution.jump([2,3,0,1,4]))

