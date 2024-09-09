**Notes:**

1. The problem asks to merge all the overlapping intervals and return an output that only contains non-overlapping intervals.
2. The most important thing to remeber whenever solving an interval problem is to visualize the number on a number line. Drawing out the problem like so will make the problem a lot easier. So when we draw out an example over the number line, we will notice that in order to merge the intervals, the input list of intervals must be sorted. If the input interval list is sorted by the start value. Then merging the intervals will become pretty straight forward.
3. So the first step to solve this problem is to sort the input where the key for sorting is the start value of the interval.
4. After that we basically need to loop over the list and start building the resultant output list of non overlapping intervals. We can intialize the output list with the first intervals. Doing this will help us in eliminating edge cases.
5. Then we go over the list starting from the index 1. Extracting the start and end of the interval. Then we take the end of the last interval currently in the output list. Then we compare whether the end of the last interval is greater or equal than the start of the interval i. If it is then we need to merge it. How do we merge it? Well we take the max of both ends of the intervals and update the end interval of the last interval in the output.
6. If the end of the last interval is smaller that the start of the interval i, then we simply add this interval to the result output. Outside the loop we wil simply return False.
7. The time complexity of this problem is O(nlogn) because of the sorting the input list. The space complexity is O(n) if we count the space used by the output list.
