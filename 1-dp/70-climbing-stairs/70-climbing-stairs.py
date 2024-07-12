class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dp(n):
            if n <= 2:
                return n
            
            if n in cache:
                return cache[n]
            
            cache[n] = dp(n - 1) + dp(n - 2)

            return cache[n]
        
        return dp(n)

#Test Case:
mySolution = Solution()
print("Test Case 1: ", mySolution.climbStairs(35))

class BU_Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one

#Test Case:
myBUSolution = BU_Solution()
print("Test Case 1: ", myBUSolution.climbStairs(35))
