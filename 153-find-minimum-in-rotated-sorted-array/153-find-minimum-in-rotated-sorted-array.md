**Notes:**

1. The most important thing in this problem is to understant what a rotated sorted array is and what do they mean by rotation. One rotation is noted by last val of the sorted array is moved to the position of the first. The problem then asks us to find the minimum value.
2. Right of the bat we can notice that the array is sorted in some way. We have to find just the minimum value. We can use this sorted property of the array and run a binary search solution with some modifications to find the minimum value.
3. In a normal binary search where the array is sorted in ascending order. The value at the left pointer is always the minimum. So basically even in this problem we can use this property of binary search.
4. Keep at resultant variable for the minimum value.
5. Run a binary search with left and right pointers set to the start and end indices of the given array. Before calculating the new mid. Check that the  value at left pointer is smaller than the value at the right pointer. If the left left most value is smaller. update the resultant min value and break the loop.
6. After calculating the mid, update the result by taking the minimum of result and the value at the mid. Because we will not be able to visit this mid value again and this mid value can be the minimum value. Consider test case `[3,1,2]`
7. Calculate the mid index of the array. Check the value at left pointer is less than equal to the value at mid pointer. If left value is less then we have to search the right side of the array. So we update the left pointer by adding one to the mid pointer.
8. If the value at left pointer in the array is greater than the value at mid pointer. It means the intersection of max and min value is on the left side of the array. So we update the right pointer by subtracting one from the mid pointer.
