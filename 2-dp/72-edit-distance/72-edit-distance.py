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




