**Notes:**

1. The brute force solution of this problem exists. It requires a nested loop where we pick a value in the outer loop and then we set the nested loop such that it starts from the next value of the picked value. This way we are not checking any the sums that are already been checked. Our check conditons compares the sum with target.
2. Brute force solution is easier to implement but has a time complexity of O(n^2). Which is not optimal.
3. In order to achieve a better time complexity, we use a Hashmap.
4. Key To Remember: `value1 + value2 = target  => target - value1 = value2`
5. So our algorithm to solve this problem is visit each value in the list. Check whether the difference yeilds any value that is already present in the hashmap. The hashmap stores array values as keys and array indices as values. {value: index}. At each iteration we store the value and index in the hashmap. If the difference yeilds a value that is present in the hashmap, we return the current index and index value from hashmap.
