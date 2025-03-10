class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        return (1 / res) if n < 0 else res
    
#Test Case 
mysolution = Solution()
print("Test Case 1: ", mysolution.myPow(2.00000, 10))
print("Test Case 1: ", mysolution.myPow(2.10000, 3))
print("Test Case 1: ", mysolution.myPow(2.00000, -2))
