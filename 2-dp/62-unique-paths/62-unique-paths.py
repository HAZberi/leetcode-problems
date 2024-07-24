class DFSSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            if r == m - 1 and c == n - 1:
                return 1
            
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]

        return dfs(0, 0)

class TabulationSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        resRow = [0] * n #previous row, starting one below from bottom

        for r in range(m - 1, -1, -1):
            curRow = [0] * n
            curRow[n - 1] = 1
            for c in range(n - 2, -1, -1):
                curRow[c] = curRow[c + 1] + resRow[c]
            resRow = curRow
        
        return resRow[0]

#Test Cases
my_dfs_solution = DFSSolution()
my_tabulation_solution = TabulationSolution()

print("test Case 1: ", my_dfs_solution.uniquePaths(3,7))
print("test Case 1: ", my_tabulation_solution.uniquePaths(3,7))
print("test Case 2: ", my_dfs_solution.uniquePaths(3,2))
print("test Case 2: ", my_tabulation_solution.uniquePaths(3,2))



