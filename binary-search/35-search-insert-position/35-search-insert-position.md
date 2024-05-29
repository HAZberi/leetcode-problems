**Notes:**

1. The problem asks us to return the index of the element if the element is equal to target. If target value is not present in the given list then we have to return the index where the target value is supposed to be (or where it should be inserted).
2. Since the given list is sorted, we can use it as our advantage and use the binary search algorithm to find the index of the target. It is quite straight forward finding the index of the target if the target exists in the list. But there are some edge cases to discuss if we are looking to find the insert position.
3. The idea is whenever our left and right pointer crosses each other, meaning we have gone through the entire list. So the position of left pointer is the one where we should insert the target value.
4. The time complexity of this algorithm is O(logn)
