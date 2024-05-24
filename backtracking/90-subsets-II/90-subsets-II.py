from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(i, subset):
            if i >= len(nums):
                result.append(subset[:])
                return
            
            #Decision to include the current element
            subset.append(nums[i])
            backtrack(i + 1, subset)

            #Decision to not inculde the current element and all of its duplicates
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return result

#Test Cases
mySolution = Solution()
print("Test Case 1: ", mySolution.subsetsWithDup([1,2,2]))
print("Test Case 2: ", mySolution.subsetsWithDup([0]))
print("Test Case 3: ", mySolution.subsetsWithDup([1,2,2,3]))