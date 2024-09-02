from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} #(index, amount): value

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount or i == len(coins):
                return 0
            if (i, a) in dp:
                return dp[(i, a)]
            
            dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return dp[(i, a)]
        
        return dfs(0, 0)

#Test Cases
mysolution = Solution()

print("Test Case 1:", mysolution.change(5, [1,2,5]))
print("Test Case 1:", mysolution.change(3, [2]))
print("Test Case 1:", mysolution.change(10, [10]))


