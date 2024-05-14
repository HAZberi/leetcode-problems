class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums) #HashSet of given nums
        longest = 0 #keeps the value of the longest consective sequence appeared

        for n in nums:
            length = 0
            if (n - 1) not in numSet:
                length += 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
            
        return longest
    

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.longestConsecutive([100,4,200,1,3,2]))
print("Test Case 2: ", mySolution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))