class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:
                threeSum = n + nums[L] + nums[R]

                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([n, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.threeSum([-1,0,1,2,-1,-4]))
print("Test Case 2: ", mySolution.threeSum([0,1,1]))
print("Test Case 3: ", mySolution.threeSum([0,0,0]))

