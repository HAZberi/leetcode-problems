**Notes**

1. The first approach is to go over a brute force solution. It requires a left pointer and a right pointer. We pick the left pointer in the outer loop and we pick the right pointer starting (left + 1) until the end of list. In this nested loop, we check and evaluate every possible combination that would give us the most area contained. First we calculate the area (which is bascially area of rectangle)by taking the difference of left and right (indexes )pointers, multiply it with the minimum height value between left and right (values at indices). Then we update the result by taking the max of current area and the last result.
2. ```python
   def maxArea(height):
   	res = 0
   	for l in range(len(height)):
   		for r in range(l + 1, len(height)):
   			area = (r - l) * min(height[r], height(l))
   			res = max(area, res)
   	return res
   ```
3. The brute force solution runs with a O(n^2) time complexity. We don't want to code up this solution even because it is very inefficient and if we try to submit it, it exceeds the maximum time limit in leetcode.
4. To achieve the run time complexity of O(n). We will have a left pointer at the start of the list and a right pointer at the end of the list. This will give us the maximum width. We calculate the area and update the result same way as we did in the brute force solution.
5. But in this case we have to update the pointers. Increment the left pointer if height at the left pointer is smaller than the height at the right pointer. Decrement the right pointer if height at the right pointer is smaller or equal than height at the left pointer.
6. Pro Tip. There is only one if - else condition. We increment the left pointer. if the value at left is smaller. Otherwise, we just need to decrement the right pointer.
