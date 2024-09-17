"""
1. Question 1
The cost of a stock on each day is given in an array, arr. 
An investor wants to buy the stocks in triplets such that 
the sum of the cost for three days is divisible by d.
The goal is to find the number of distinct triplets (i,j,k) 
such that i<j<k and the sum (a[i]+a[j]+a[k]) is divisible by d.
Example
Let arr, prices of stock = [3, 3, 4, 7, 8] and d=5. 
Following are the triplets whose sum is divisible by d (1-based indexing):
• Triplet with indices-(1, 2, 3), sum = 3+3+4 which is equal to 10
• Triplet with indices-(1, 3, 5), sum =3+4+8 which is equal to 15 
 Triplet with indices-(2, 3, 4), sum = 3+4+8 which is equal to 15
Hence the answer is 3.
"""
from typing import List


def findTheTriplets(price: List[int], d:int):
    res = 0
    test = []

    #Edge Case if the size is not given.
    if (len(price) < 3):
        return 0

    for i in range(len(price) - 2):
        l = i + 1
        r = len(price) - 1

        while l < r:
            threeSum = price[i] + price[l] + price[r]
            if (threeSum % d) == 0:
                res += 1
                test.append(((i, l, r), threeSum))
            l += 1

        l = i + 1
        r = len(price) - 2

        while l < r:
            threeSum = price[i] + price[l] + price[r]
            if (threeSum % d) == 0:
                res += 1
                test.append(((i, l, r), threeSum))
            r -= 1
    
    return [res, test] #Note in the original question we only need to return "res"

#Test Case 
print("Test Case 1:", findTheTriplets([3,3,4,7,8], 5))
print("Test Case 2:", findTheTriplets([2,6,2,2,6,7,8,3,4], 5))


