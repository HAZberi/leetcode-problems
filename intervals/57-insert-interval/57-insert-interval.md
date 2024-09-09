**Notes:**

1. The problem asks us to insert a newinterval into a sorted list of intervals such that there are no overlapping intervals and the order is also maintained. We are allowed to merge overlapping intervals.
2. The first thing we have to notice is to explore all the possibilities of inserting a new interval. If we are looping over the list of intervals. Following are the cases that are possible. This helps in understanding the problem better.
   1. End of new interval is smaller than the start of an interval i. It means we can safely insert the new interval to the result.
   2. Start of new interval is greater than the end of an interval i. It means we can safely add the interval i to the result.
   3. Anything else here basically means we have to merge the intervals.
3. We have to maintain a resultant list where we keep on adding the intervals. While traversing the list of intervals, if the first condition satifies, it will mean that we can add the new interval to the result and also add all the remaining intervals to result. Immediately we can return the result because we have found the solution.
4. For the second condition the new interval is greater than the interval i. So we simply add it to the result.
5. Now the special case where start of new interval is smaller than the end of interval or end of new interval is greater than the start of interval i or any combination, then it means we need to merge the two intervals and important thing is that we will not add the merged interval in the result. Why? because this merged interval can be overlapping with other intervals down the list. So what should we do? We will simply update the newInterval with this merged interval.
6. How do we merge two intervals?
   ```
   merged = [min of starts, max of ends]
   ```
7. There is one more important thing that we should do, if we ever come out of the loop that traverses the list. First we need to understand when will this happen? This will happen only if the new/updated interval is not added to the result, because if we have added the newinterval, we would have added the remaining intervals and returned the result right away. If this doesnt happens and we come out of a loop then it means that the newinterval/updated interval is the last interval in our result. So we need to add this last interval to the result and only then we will return the result.
8. The time complexity of this solution is O(n) since we traverse the list only once. The space complexity is O(n) since we build up the result in a new list.
