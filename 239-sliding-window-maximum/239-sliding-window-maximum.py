from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        L = 0
        que = deque()

        for R in range(len(nums)):
            while que and nums[que[-1]] < nums[R]:
                que.pop()
            que.append(R) #Just storing the index in the queue. We can retrieve nums using the indices.

            if L > que[0]: #Left pointer is greater than the index val at the left of the que. That's how we know our window has moved. 
                que.popleft()
            
            if (R - L + 1) == k:
                res.append(nums[que[0]]) #leftmost index is the maximum
                L += 1
        
        return res

#Test Cases

mySolution = Solution()
print("Test Case 1: ", mySolution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print("Test Case 2: ", mySolution.maxSlidingWindow([1], 1))
print("Test Case 3: ", mySolution.maxSlidingWindow([8,7,6,9], 2))