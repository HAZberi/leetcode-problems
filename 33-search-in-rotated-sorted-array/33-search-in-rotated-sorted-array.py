from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while (l <= r):
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: #left sorted portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: #right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1
        
        return -1
    
#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.search([4,5,6,7,0,1,2], 0))
print("Test Case 2: ", mySolution.search([4,5,6,7,0,1,2], 6))
print("Test Case 3: ", mySolution.search([1], 0))