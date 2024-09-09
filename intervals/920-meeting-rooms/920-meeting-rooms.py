from typing import (
    List,
)


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda i: i.start)
        prevEnd = intervals[0].end
        
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i].start:
                return False
            prevEnd = intervals[i].end
        
        return True
    
#Test Case 
mysolution = Solution()
print("Test Case 1: ", mysolution.can_attend_meetings([Interval(0,30),Interval(5,10),Interval(15,20)]))    
print("Test Case 2: ", mysolution.can_attend_meetings([Interval(5,8),Interval(9,15)]))    
print("Test Case 3: ", mysolution.can_attend_meetings([Interval(5,8),Interval(8,15)]))    