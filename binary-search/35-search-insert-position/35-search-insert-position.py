from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1 
        
        return L

#Test Cases
mySolution = Solution()
print("Test Case 1: ", mySolution.searchInsert([1,3,5,6], 5))
print("Test Case 2: ", mySolution.searchInsert([1,3,5,6], 2))
print("Test Case 3: ", mySolution.searchInsert([1,3,5,6], 7))
