**Notes:**

1. In this we are given a sorted array that is rotates at some index. The task is to find the index of a target value. We can use the sorted property to our advantage and would be able to use a binary search algorithm and achieve a run time complexity of O(logn).
2. We can start running a binary search on the entire array. Left pointer, Right pointer, while loop where left is less than equal to right. Inside the the loop we will calculate the mid.
3. If the target is equal to mid value we will just return the mid.
4. If the value at mid is greater than the value at left, it means we are on the left sorted portion of the array. If the value at mid is smaller than the value at left, it means we are on the right sorted portion of the array.
5. If value at mid is greater than the value at left (Left sorted Portion). We will have following conditions
   1. If target is greater than mid value, we will then choose the right side of the array. `l = mid + 1`
   2. If target is greater than left value, we will then choose the left side of the array. `r = mid - 1`
   3. If target is smaller than left value, we will then choose the right side of the array. `l = mid + 1`
6. If value at mid is smaller than value at the left (Right sorted Portion). We will have following conditions
   1. if target is greater than mid value, we will then choose the right side of the array `l = mid + 1`
   2. if target is greater than right value, we will then choose the left side of the array `r = mid - 1`
   3. if target is smaller than right value, we will then choose the right side of the array `l = mid + 1`
