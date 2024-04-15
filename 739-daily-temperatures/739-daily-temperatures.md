**iNotes:**

1. The problem ask us to find the next warmer day in the list. So a simple brute force solution would suggest a nested loop, where we compare each value with entire list and as soon as we hit a warmer day. We store the difference of indices in the resultant array. This would be O(n^2)
2. In order to improve the time complexity, we can use help of data structure, which increases the space complexity to O(n) but time complexity can be improved to O(n).
3. When we traverse the list from left to right in a loop. We can put values on to the stack.
4. If the stack is not empty, then we can check whether current value is greater than the value on the stack. If current value is greater then, we pop out last value from stack, take a difference of current index with the index of the popped out value from stack. We store this difference in the resultant array at the same index as the index of the popped out value. We need to keep doing these operations until current value is smaller then the last value on the stack.
5. If the current value is smaller then the value at the top of the stack. We will keep on adding values on to the stack.
6. By the end, number of days to next warmer day is populated on to the resultant array. If there are no warmer days, for example the last value in the given input list, we will just use the default value of zero.
7. Pro Tip: Initialize the resultant array with pre-populated default value of zero.
