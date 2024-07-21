from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(1, n + 1):
            countI = 0
            j = i
            while j > 0:
                countI += j % 2
                j = j // 2 #logn increment
            res.append(countI)
        
        return res

class DPSolution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

#Test Case
my_solution = Solution()
my_dpsolution = DPSolution()

print("Test Case 1: ", my_solution.countBits(2))
print("Test Case 1: ", my_dpsolution.countBits(2))
print("Test Case 2: ", my_solution.countBits(5))
print("Test Case 2: ", my_dpsolution.countBits(5))
print("Test Case 2: ", my_solution.countBits(8))
print("Test Case 2: ", my_dpsolution.countBits(8))
            

        