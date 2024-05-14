class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L , R = 0, len(numbers) - 1

        while L < R: 
            currSum = numbers[L] + numbers[R]

            if currSum > target:
                R -=1
            elif currSum < target:
                L +=1
            else:
                return [L + 1, R + 1]

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.twoSum([2,7,11,15], 9))
print("Test Case 1: ", mySolution.twoSum([2,3,4], 6))
print("Test Case 1: ", mySolution.twoSum([-1,0], -1))
