from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        i, carry = 0, 1

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(carry)
                carry = 0
            i += 1
        
        return digits[::-1]

#Test Case 
my_solution = Solution()
print("Test Case 1: ", my_solution.plusOne([1,2,3]))
print("Test Case 2: ", my_solution.plusOne([4,3,2,1]))
print("Test Case 3: ", my_solution.plusOne([9,9,9,9]))


