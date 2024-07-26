import math


class Solution:
    def reverse(self, x: int) -> int:
        # Interger.MIN_VaLUE = -2147483648
        # Interger.MAX_VaLUE = 2147483647
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x != 0: #we cannot say x > 0 because x can be negative as well.
            digit = int(math.fmod(x, 10)) #python is dumb because -1 % 10 = 9
            x = int(x / 10)               #python is dumb because -1 // 10 = -1

            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0

            res = (res * 10) + digit
        
        return res
    
#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.reverse(123))
print("Test Case 2: ", my_solution.reverse(-123))
print("Test Case 3: ", my_solution.reverse(120))
print("Test Case 4: ", my_solution.reverse(1534236469))




