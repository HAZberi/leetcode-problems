from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        cache = {}
        def dp(n):
            if n <= 1:
                return cost[n]
            
            if n in cache:
                return cache[n]
            
            cache[n] = cost[n] + min(dp(n - 1), dp(n - 2))

            return cache[n]
        
        return dp(len(cost) - 1)

#Test Case:
my_solution = Solution()
print("Test Case 1: ", my_solution.minCostClimbingStairs([10,15,20]))
print("Test Case 1: ", my_solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
