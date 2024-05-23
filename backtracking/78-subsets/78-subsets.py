from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #To include the current number in the subset
            subset.append(nums[i])
            backtrack(i + 1)

            #Not including the cureent number in the subset
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res

#Test Cases
mySolution = Solution()
print("Test Case 1: ", mySolution.subsets([1,2,3]))
print("Test Case 2: ", mySolution.subsets([0]))