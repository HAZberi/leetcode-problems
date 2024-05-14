**Notes:** 

1. Product of all the values except the value currently at the index. The answer array store the product of all values expect the value currently at the index at the same index. For Example `arr = [1,2,3,4], ans = [24,12,8,6]`.
2. If we take the product of entire array and divide the product by each value. We will get the answer array. But this approach is specifically not allowed.
3. The time complexity should be O(n) and we are also aiming to minimize the space complexity to O(n).
4. ProTip: For each value, we can compute the product prefix of all the values before it and we can also compute the product postfix of all the values after it. Then we multiply the product prefix before the value with the product postfix after the value. The result can be placed at the same index (index of value we compute prefix and postfix) in the resultant array.
5. One way to approach the above is to create a seprate product prefix and product postfix arrays. Then multipy the prefix of before values with postfix of after values and store the result in the array. This increases our space complexity to O(n).
6. It is possible to do a couple of passes. First pass to store the product prefix of all the previous values at the same index in the result array. Then in the second pass MULTIPLY the product postfix (using a reverse loop) of all the upcoming values with the existing product prefix value. Return the answer.
