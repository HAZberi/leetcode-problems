**Notes:**

1. The problem ask us to multiply two strings of integers without using any BigInt libraries and return the result in strings.
2. We have to recall the algorithm of multiplication we used in our elementary school here to multiply the numbers and find some appropriate structures and logical steps to convert that algorithm into code.
3. The first edge case of this problem is if any of the strings are "0", this means multiplication is not possible. So we immidiately return "0".
4. Then we have to reverse the strings. Also we have to create a resultant array where we will store the digits of the final result and then convert the resultant digits into string and join it. We initialize the resultant array with 0 values, we will be overwriting these value by adding to it as we process the multiplication. The length of the resultant array should be the sum of the lengths of two strings, because that would the maximum number of digits possible when multiplying two numbers.
5. We will be generating the resultant array in reverse order. Once the multiplication process is complete we will simply reverse the list and convert it to string.
6. Each digit will be multiplied with all the digits of the other number. So this means that for multiplication we must need a nested loop. Then we have to follow the following process
   1. Multiply the two digits by converting them to integers and add it to the resultant list at the index that is sum of the indices of two source digits. [Multiplication Step]
   2. Then at the next index of the current index in the resultant list, we add the ten's place digit of the recently computed number. [Carry Adjustment]. x // 10 to get ten's place.
   3. Then we replace the value at the current index in the resultant list with the unit's place digit of the recently computer number. [Unit's Place Adjustment]. x % 10 to get unit's place.
7. Once we have completed the multiplication process and populated the resultant list. We reverse the resultant list and remove all leading zeros. Use a pointer that tracks the begining of the non-zero value and then slice the array from that point.
8. After that map each value in the resultant with str() function. This will convert all the interger values in the resultant list to strings. Then simply join the strings and return the result.
9. The time complexity of this solution is O(m.n) and the space complexity is O(m + n)
