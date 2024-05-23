from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curComb, total):
            if total == target:
                res.append(curComb.copy())
                return 
            
            if i >= len(candidates) or total > target:
                return
            
            #Decision to include the same element 
            curComb.append(candidates[i])
            backtrack(i, curComb, total + candidates[i])

            #Decision to not include the same element
            curComb.pop()
            backtrack(i + 1, curComb, total)
        
        backtrack(0, [], 0)
        return res

#Test Cases
mySolution = Solution()
print("Test Case 1: ", mySolution.combinationSum([2,3,6,7], 7))
print("Test Case 2: ", mySolution.combinationSum([2,3,5], 8))
print("Test Case 3: ", mySolution.combinationSum([2], 1))
