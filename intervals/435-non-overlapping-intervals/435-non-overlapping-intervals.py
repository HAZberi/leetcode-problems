from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda i: i[0])

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if prevEnd > start:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        
        return res

#Test Case 
mysolution = Solution()
print("Test Case 1: ", mysolution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print("Test Case 2: ", mysolution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print("Test Case 3: ", mysolution.eraseOverlapIntervals([[1,2],[2,3]]))
