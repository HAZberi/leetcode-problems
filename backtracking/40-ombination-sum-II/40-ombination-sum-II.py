from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, subset, total):
            if total == target:
                res.append(subset[:])
                return 
            
            if i >= len(candidates) or total > target:
                return 
            
            #Decision to inculde the current element
            subset.append(candidates[i])
            backtrack(i + 1, subset, total + candidates[i])

            #Decision to not include the current element and all of its duplicates
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, subset, total)
        
        backtrack(0,[],0)
        return res

#Test Cases:
mySolution = Solution()
print("Test Case 1: ", mySolution.combinationSum2([10,1,2,7,6,1,5], 8))
print("Test Case 2: ", mySolution.combinationSum2([2,5,2,1,2], 5))