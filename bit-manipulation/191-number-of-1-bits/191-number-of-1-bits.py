class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n >> 1
        return count

class CleverSolution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count

#Test Case:
my_solution = Solution()
my_clever = CleverSolution()

print("Test Case 1: ", my_solution.hammingWeight(11))
print("Test Case 1: ", my_clever.hammingWeight(11))
print("Test Case 2: ", my_solution.hammingWeight(128))
print("Test Case 2: ", my_clever.hammingWeight(128))
print("Test Case 3: ", my_solution.hammingWeight(2147483645))
print("Test Case 3: ", my_clever.hammingWeight(2147483645))



