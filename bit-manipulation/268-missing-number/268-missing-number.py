from typing import List


class HashsetSolution:
    def missingNumber(self, nums: List[int]) -> int:
        rangeSet = set([i for i in range(len(nums) + 1)])
        for i in range(len(nums)):
            if nums[i] in rangeSet:
                rangeSet.remove(nums[i])

        return rangeSet.pop()

class XORSolution:
    def missingNumber(self, nums: List[int]) -> int:
        xorSum = len(nums)
        for i in range(len(nums)):
            xorSum = xorSum ^ (i ^ nums[i])
        
        return xorSum

class SumSolution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res


#Test Cases
my_hashset_solution = HashsetSolution()
my_xor_solution = XORSolution()
my_sum_solution = SumSolution()

print("Test Case 1: ", my_hashset_solution.missingNumber([3,0,1]))
print("Test Case 1: ", my_xor_solution.missingNumber([3,0,1]))
print("Test Case 1: ", my_sum_solution.missingNumber([3,0,1]))
print("Test Case 2: ", my_hashset_solution.missingNumber([0,1]))
print("Test Case 2: ", my_xor_solution.missingNumber([0,1]))
print("Test Case 2: ", my_sum_solution.missingNumber([0,1]))
print("Test Case 3: ", my_hashset_solution.missingNumber([9,6,4,2,3,5,7,0,1]))
print("Test Case 3: ", my_xor_solution.missingNumber([9,6,4,2,3,5,7,0,1]))
print("Test Case 3: ", my_sum_solution.missingNumber([9,6,4,2,3,5,7,0,1]))

