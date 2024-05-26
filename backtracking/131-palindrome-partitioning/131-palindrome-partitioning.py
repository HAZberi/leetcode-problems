from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(i):
            if i >= len(s):
                res.append(partition[:])
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i: j+1])
                    backtrack(j + 1)
                    partition.pop()

        backtrack(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while (l < r):
            if s[l] != s[r]:
                return False         
            l += 1
            r -= 1
            
        return True
    
#Test Cases:
mySolution = Solution()
print("Test Case 1: ", mySolution.partition("aab"))
print("Test Case 2: ", mySolution.partition("a"))
print("Test Case 3: ", mySolution.partition("aaba"))