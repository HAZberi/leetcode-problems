class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {} #{value: index} of visited elements in the nums array

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i

#TestCases
mySolution = Solution()

print("Test Case 1:", mySolution.twoSum([2,7,11,15], 9))
print("Test Case 2:", mySolution.twoSum([3,2,4], 6))
print("Test Case 3:", mySolution.twoSum([3,3], 6))