from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

#Test Case:
my_solution = Solution()
print("Test Case 1: ", my_solution.wordBreak("leetcode", ["leet","code"]))
print("Test Case 2: ", my_solution.wordBreak("applepenapple", ["apple","pen"]))
print("Test Case 3: ", my_solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

