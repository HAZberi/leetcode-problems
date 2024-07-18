from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    res.add(i)

        return len(res) == 3

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
print("Test Case 2: ", my_solution.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))
print("Test Case 3: ", my_solution.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))

