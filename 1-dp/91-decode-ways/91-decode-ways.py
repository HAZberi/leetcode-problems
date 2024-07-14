class TDSolution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)

#Test Case:
my_solution_td = TDSolution()
print("Test Case 1: ", my_solution_td.numDecodings("12"))
print("Test Case 2: ", my_solution_td.numDecodings("226"))
print("Test Case 3: ", my_solution_td.numDecodings("06"))
print("Test Case 4: ", my_solution_td.numDecodings("301"))
print("Test Case 5: ", my_solution_td.numDecodings("1212"))
print("Test Case 6: ", my_solution_td.numDecodings("12121"))

class BUSolution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                    dp[i] += dp[i + 2]
        
        return dp[0]

#Test Case:
my_solution_bu = BUSolution()
print("Test Case 1: ", my_solution_bu.numDecodings("12"))
print("Test Case 2: ", my_solution_bu.numDecodings("226"))
print("Test Case 3: ", my_solution_bu.numDecodings("06"))
print("Test Case 4: ", my_solution_bu.numDecodings("301"))
print("Test Case 5: ", my_solution_bu.numDecodings("1212"))
print("Test Case 6: ", my_solution_bu.numDecodings("12121"))