
from typing import List

"""
Definition of Interval:
"""
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        
        return res

#Test Case 
mysolution = Solution()
print("Test Case 1:", mysolution.minMeetingRooms([Interval(0,40),Interval(5,10),Interval(15,20)]))
print("Test Case 2:", mysolution.minMeetingRooms([Interval(4,9)]))
