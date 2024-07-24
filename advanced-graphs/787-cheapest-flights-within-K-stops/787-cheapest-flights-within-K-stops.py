from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tempPrices = prices.copy()
            for u, v, cost in flights:
                if prices[u] + cost < prices[v]:
                    tempPrices[v] = prices[u] + cost 
            prices = tempPrices
        
        return prices[dst] if prices[dst] != float("inf") else -1

#Test Cases:
my_soltution = Solution()
print( "Test Case 1: ", my_soltution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
print( "Test Case 2: ", my_soltution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
print( "Test Case 3: ", my_soltution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))


