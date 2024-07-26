class TopDownSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if len(word1[i:]) == 0: 
                cache[(i, j)] = len(word2[j:])
                return cache[(i, j)]
            if len(word2[j:]) == 0:
                cache[(i, j)] = len(word1[i:])
                return cache[(i, j)]
            
            cache[(i, j)] = 0
            if word1[i] == word2[j]:
                cache[(i, j)] += dfs(i + 1, j + 1)
            else:
                cache[(i, j)] += 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
            
            return cache[(i, j)]
        
        return dfs(0, 0)
    
#Test Case
my_topDown_solution = TopDownSolution()
print("Test Case 1: ", my_topDown_solution.minDistance("horse", "ros"))
print("Test Case 2: ", my_topDown_solution.minDistance("intention", "execution"))


class BottomUpSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        
        print(dp)

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]

#Test Case
my_bottomUp_solution = BottomUpSolution()
print("Test Case 1: ", my_bottomUp_solution.minDistance("horse", "ros"))
print("Test Case 2: ", my_bottomUp_solution.minDistance("intention", "execution"))

