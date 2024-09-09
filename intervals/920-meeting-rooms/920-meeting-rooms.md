**Notes:**

1. The problem asks us to find out whether there is a conflict in meetings given a list of intervals.
2. So the basic idea here is to make sure that the list of intervals is sorted. This is the bottle neck of out solution.
3. Once we have sorted the intervals. Then we iterate over the sorted list of intervals. Please note that intervals are represented as object. So we have to use the syntax that is more supportive for object.
4. How do we know if there is a conflict. We have to compare the adjacent intervals. So we will compare the end of the previous interval with the start of the next interval. If the previous end of the interval is greater than the start of the next interval. It means the person cannot attend the next meeting becuase the previous meeting is still going. So we have a conflict and we can immidiately return false. If thats not the case, then we can simply update the previous end with the current end and continue to iterate.
5. Once we break out of the loop, we will simply return True. Since if there was a conflict we would have returned false right away.
6. The time complexity of this solution is O(nlogn) because of sorting. The space complexity is O(1)
