class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        res = nums[0]

        while (l <= r):
            if (nums[l] <= nums[r]):
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if (nums[l] <= nums[mid]):
                l = mid + 1
            else:
                r = mid - 1

        return res

#Test Case

mySolution = Solution()

print("Test Case 1: ", mySolution.findMin([3,4,5,1,2]))
print("Test Case 2: ", mySolution.findMin([4,5,6,7,0,1,2]))
print("Test Case 3: ", mySolution.findMin([11,13,15,17]))
