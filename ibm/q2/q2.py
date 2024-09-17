"""
2. Question 2
For each element of an array, a counter is set to 0. 
The element is compared to each element to its left. 
If the element to the left is greater, the absolute difference 
is subtracted from the counter. If the element to the left is less, 
the absolute difference is added to the counter. For each element of 
the array, determine the value of the counter. 
These values should be stored in an array and returned.
Example
n = 3, the number of elements
arr = [2, 4, 3]
For arr[0]=2, counter starts at 0 and there are no elements to the 
left so counter = 0.
• For arr[1]-4, counter starts at 0 and 
then Increases by | 4-2 | = 2 at the first and only comparison: 
counter - 2.
Testing am[2]=3, first against 4, counter = 0-13- 4)-1, 
and then against 2 counter =-1+13-21-
0.
• The answer array is [0. 2. 0].
"""

def arrayChallenge(nums: list[int]):
    res = []
    res.append(0)

    for i in range(1, len(nums)):
        count = 0
        for j in range(0, i):
            diff = nums[i] - nums[j]
            count += diff
        res.append(count)
    
    return res

#Test Case
print("Test Case 1:", arrayChallenge([2,1,3]))
print("Test Case 2:", arrayChallenge([2,4,3]))
print("Test Case 3:", arrayChallenge([2,4,3,7,2]))


