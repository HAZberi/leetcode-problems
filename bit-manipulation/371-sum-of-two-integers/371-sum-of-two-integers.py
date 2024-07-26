class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff #creates a 32 bit format
        while b != 0:
            temp = (a & b) << 1
            a = (a ^ b) & mask
            b = temp & mask
        
        if a > mask // 2: #the result "a" comes out to be negative
            return ~(a ^ mask)
        else: #the result "a" comes out to be positive
            return a

#Test Case 
my_solution = Solution()
print("Test Case1: ", my_solution.getSum(9, 11))
print("Test Case2: ", my_solution.getSum(2, 3))
print("Test Case3: ", my_solution.getSum(2, -3))

        
