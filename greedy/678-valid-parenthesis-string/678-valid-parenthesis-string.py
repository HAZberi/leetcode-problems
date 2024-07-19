class RecursiveSolution:
    def checkValidString(self, s: str) -> bool: #O(n ^ 3)
        dp = {(len(s), 0): True} #[(index, leftcount): Bool]

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]
            
            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = dfs(i + 1, left - 1) or dfs(i + 1, left + 1) or dfs(i + 1, left)
            
            return dp[(i, left)]
        
        return dfs(0,0)

class GreedySolution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if leftMax < 0: #We have more closed parenthesis 
                return False
            if leftMin < 0: #We have turned every asterick in a closed parenthesis
                leftMin = 0 #We have used a asterick and give it a chance to be valid
            
        return leftMin == 0 #If the left min is posiitve it means that we have less closed parenthesis


