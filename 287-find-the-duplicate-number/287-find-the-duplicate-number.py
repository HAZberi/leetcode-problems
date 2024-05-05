from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

#Test Cases
mySolution = Solution()

print("Test Case 1: ", mySolution.findDuplicate([1,3,4,2,2]))
print("Test Case 2: ", mySolution.findDuplicate([3,1,3,4,2]))
print("Test Case 3: ", mySolution.findDuplicate([3,3,3,3,3]))