import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = max(piles)

        while (l <= r):
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += (math.ceil(p / k))
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res

#Test Cases:

mySolution = Solution()

print("Test Case 1", mySolution.minEatingSpeed([3,6,7,11], 8))
print("Test Case 2", mySolution.minEatingSpeed([30,11,23,4,20], 5))
print("Test Case 3", mySolution.minEatingSpeed([30,11,23,4,20], 6))