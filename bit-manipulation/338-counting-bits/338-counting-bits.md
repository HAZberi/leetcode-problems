**Notes:** 

1. The problem asks us to create an array of n + 1 length where each index represent a value between the range 0-n, where n is given. And the corresponding values of these indices represents the total number of binary 1s for that index.
2. We have two soliutions to this problem, the first solution is O(nlogn). Basically for each number in the range of 0 - n, We keep on integer dividing the number by 2 until it becomes 0, and at each step take the modulus of the number with 2 and add it to the 1s count for the number. After the number becomes zero, we append the count to our resultant list. Since we have to go through each element once and then for each element we divide it by by 2 until it became 0, so this will be O(logn) in time complexity. So overall time complexity of this problem is O(n.logn)
3. The second soltuion is the most optimal solution O(n) but it requires dynamic programming, we have to find a pattern so we can cache our previous results. Even in the result array, we are supposed to gets 1s count of the value at each index. Can we use it as dp array and some how use the previous results to calculate new results. The answer is yes.
4. The best to illustrate this is to draw a n = 8 converison to binary from (0 - 8). We will notice all significant values has only one 1 bit. So all the numbers after the significant numbers are basically the 1 plus the result of the difference of current value and the offset. Offset is basically the significant numbers. So our dp equation for this problem is going to be `dp[i] = 1 + dp[i - offset]`
5. We keep a dp array, which will be our result as well. We initialize our dp array with fist value as zero. We intialize the offset = 1.
6. So we simply loop the range starting from 1- n+1. Then we wiill check if offset * 2 is equal to current i. Offset can be found out by simply multiplying the previous offset by 2. if the current number is the new offset, we will simply update the offset. After that we set the value for this current i in our dp array and using the dp equation disscussed above. Outside the loop we will simply return the dp array.