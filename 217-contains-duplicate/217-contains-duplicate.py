class Solution(object):
    def containsDuplicate(self, nums) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        
        return False
    
#Test Cases

mySolution = Solution()

print("Test Case 1:", mySolution.containsDuplicate([1,2,3,1]))
print("Test Case 2:", mySolution.containsDuplicate([1,2,3,4]))
print("Test Case 3:", mySolution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))