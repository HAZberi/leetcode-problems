class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        
        return res
    
#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.reverseBits(43261596))
print("Test Case 2: ", my_solution.reverseBits(4294967293))

