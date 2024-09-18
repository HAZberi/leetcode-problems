"""
Odd-Even-Transform Problem works on an array of integers 
(both positive, negative, and zero), by taking in a value 
(a whole number) that specifies the number of times the transformation
has to be applied.
On an array of integers, the transformation that n number of times 
needs to occur:
- Adds three (+3) to each odd integer.
- Subtracts three (-3) from each even integer.
Example:
[3, 4, 9] means the array with integers 3, 4, 9 has to undergo 
transformation 3 times.
[3, 4, 9] -> [6, 1, 12] -> [3, 4, 9] -> [6, 1, 12]. 
So the result is [6, 1, 12].
"""

from typing import List


def oddEvenTransform(nums:List[int], n:int):
    if n % 2 == 0:
        return nums
    
    res = []
    for num in nums:
        if num % 2 == 0:
            res.append(num - n)
        else:
            res.append(num + n)
    
    return res

#Test Case 
print("Test Case 1: ", oddEvenTransform([3,4,9], 98))



