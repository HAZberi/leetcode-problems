class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)): #prefix pass
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #postfix pass
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.productExceptSelf([1,2,3,4]))
print("Test Case 2: ", mySolution.productExceptSelf([-1,1,0,-3,3]))