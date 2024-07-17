from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        total_balance = 0
        for i in range(len(cost)):
            total_balance += gas[i] - cost[i]
            
            if total_balance < 0:
                start = i + 1
                total_balance = 0
        
        return start


#Test Case:
my_solution = Solution()
print("Test Case 1: ", my_solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print("Test Case 2: ", my_solution.canCompleteCircuit([2,3,4], [3,4,3]))
print("Test Case 3: ", my_solution.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
