from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.coinChange([1,2,5], 11))
print("Test Case 2: ", my_solution.coinChange([2], 3))
print("Test Case 3: ", my_solution.coinChange([1], 0))



