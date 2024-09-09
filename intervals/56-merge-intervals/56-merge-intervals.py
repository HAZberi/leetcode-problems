from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nLogn)
        intervals.sort(key=lambda i: i[0])

        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if lastEnd >= start:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        
        return res
    
#Test Case 
mysolution = Solution()
print("Test Case 1: ", mysolution.merge([[1,3],[2,6],[8,10],[15,18]]))
print("Test Case 2: ", mysolution.merge([[1,4],[4,5]]))
print("Test Case 3: ", mysolution.merge([[1,3],[8,10],[15,18],[2,7]]))


