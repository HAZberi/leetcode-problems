class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums)

        while (L <= R):
            mid = (L + R) // 2

            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid
        
        return -1

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.search([-1,0,3,5,9,12], 9))
print("Test Case 2: ", mySolution.search([-1,0,3,5,9,12], 2))