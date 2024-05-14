
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        L = 0

        for R in range(1, len(prices)):
            if prices[L] >= prices[R]:
                L = R
            else:
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
        
        return maxProfit

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.maxProfit([7,1,5,3,6,4]))
print("Test Case 2: ", mySolution.maxProfit([7,6,4,3,1]))