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

class BUSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) #Top floor cost added.
        n = len(cost)
        first, second = cost[n - 2], cost[n - 1]
        
        for i in range(n - 3, -1, -1):
            temp = first
            first = cost[i] + min(first, second)
            second = temp
        
        return min(first, second)

#Test Case:
my_busolution = BUSolution()
print("Test Case 1: ", my_busolution.minCostClimbingStairs([10,15,20]))
print("Test Case 1: ", my_busolution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

class NeetCodeSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) #Top floor cost added.
       
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])

#Test Case:
neetcode_busolution = NeetCodeSolution()
print("Test Case 1: ", neetcode_busolution.minCostClimbingStairs([10,15,20]))
print("Test Case 1: ", neetcode_busolution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))