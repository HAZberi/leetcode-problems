from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res
    

#Test cases
mysolution = Solution()
print("Test Case 1: ", mysolution.insert([[1,3],[6,9]], [2,5]))
print("Test Case 2: ", mysolution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [2,5]))
print("Test Case 3: ", mysolution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

