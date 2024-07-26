**Notes:** 

1. The problem asks us to reverse a given interger x, such that if the reversed output goes beyond the range of the signed 32 bit interger [-2^31, 2^31 - 1].
2. Lets discuss how we can reverse an interger if we dont have constraint ourselves with the given range. After that we will incorporate the range as well.
3. So we have a given integer x, we want to get its last digit, how can we do that. We take the mod of x with 10 and we will have the last digit. We can store this last digit in some result variable. Then in order to take the remaining digits we have to divide the x by 10 (integer division). We will get the remaining digits and the last digit of x is omitted, basically at this step we have transformed the x.
4. Now inorder to add the next digit from the remaining digits of x. Again we take the mod the x by 10 to get the last digit of the current x. But we need it to put it as the last digit of the result. How can we do that?. If we multiply the result with 10, it shifts the current digit to left by 1 and add a zero at the last digit. This is exactly what we want. Now we simply add the chopped off digit to the result and continue to the next iteration. A simple breakdown of this algorithm is given below.

   ```
   x = 123

   res = 0
   123 % 10 = 3		res = (0 * 10) + 3 = 3 
   123 / 10 = 12		x = 12
   12 % 10  = 2		res = (3 * 10) + 2 = 32
   12 / 10	 = 1		x = 1
   1 % 10 	 = 1		res = (32 * 10) + 1 = 321 #result have the reversed integers
   1 / 10 	 = 0 #x becomes 0		 
   ```
5. Now we have our reverse algorithm in place, now we need to incorporate the range. The resulting interger should be in the range of [-2^31, 2^31 - 1], which can also be represented as -2147483648, +2147483647.
6. So the idea is that we chop off the the last digit from the MIN or MAX range and compare it with the result, if our result is already greater or lesser than 214748364, we will return 0. To chop off the last digit we divide it by 10.
7. There is one more condition, what if our result is equal to +-214748364 (chopped off last digit) then we have to check the incoming digit that we are about to add to our result. That digit must be greater or less than the last digit of MIN and MAX. If not then we will return 0.
8. We have to address these edge cases before adding any digit to the result.
