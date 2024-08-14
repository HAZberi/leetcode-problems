from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #key = (i, buying), value = max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cool = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cool)
            else:    
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cool)

            return dp[(i, buying)]
        
        return dfs(0, True)

#Test Cases
my_solution = Solution()
print("Test Case 1:", my_solution.maxProfit([1,2,3,0,2]))
print("Test Case 2:", my_solution.maxProfit([1]))

