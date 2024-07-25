class TopDownSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            
            return cache[(i, j)]
        
        return dfs(0, 0)

#Test Cases:
my_topDown_solution = TopDownSolution()
print("Test Case 1: ", my_topDown_solution.longestCommonSubsequence("abcde", "ace"))
print("Test Case 2: ", my_topDown_solution.longestCommonSubsequence("abc", "abc"))
print("Test Case 3: ", my_topDown_solution.longestCommonSubsequence("abc", "def"))


class BottomUpSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]

#Test Cases:
my_bottomUp_solution = BottomUpSolution()
print("Test Case 1: ", my_bottomUp_solution.longestCommonSubsequence("abcde", "ace"))
print("Test Case 2: ", my_bottomUp_solution.longestCommonSubsequence("abc", "abc"))
print("Test Case 3: ", my_bottomUp_solution.longestCommonSubsequence("abc", "def"))

