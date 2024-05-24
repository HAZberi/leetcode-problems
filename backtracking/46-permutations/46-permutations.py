from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]
        
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            result.extend(perms)
            nums.append(n)
        
        return result

class OtherSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i):
            if i >= len(nums):
                return [[]]
            
            resPerms = []
            perms = backtrack(i + 1)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p[:]
                    pCopy.insert(j, nums[i])
                    resPerms.append(pCopy)
            
            return resPerms
        
        return backtrack(0)

#Test Cases
mySolution = Solution()
myOtherSolution = Solution()
print("Test Case 1: ", mySolution.permute([1,2,3]))
print("Test Case 1: ", myOtherSolution.permute([1,2,3]))
print("Test Case 2: ", mySolution.permute([1,2,3,4]))
print("Test Case 2: ", myOtherSolution.permute([1,2,3,4]))
print("Test Case 3: ", mySolution.permute([1]))
print("Test Case 3: ", myOtherSolution.permute([1]))