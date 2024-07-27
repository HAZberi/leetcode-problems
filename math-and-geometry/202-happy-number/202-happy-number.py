class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False
    

    def sumOfSquares(self, n: int) -> int:
        output = 0
        
        while n:
            digit = n % 10
            output += (digit ** 2)
            n = n // 10
        return output

#Test Case
my_solution = Solution()
print("Test Case 1: ", my_solution.isHappy(19))
print("Test Case 2: ", my_solution.isHappy(2))

