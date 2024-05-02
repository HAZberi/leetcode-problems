class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(t)
        res = [-1, -1]
        resLen = float("inf")
        L = 0
        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)

            if s[R] in countT and countT[s[R]] == window[s[R]]:
                have += 1
            
            while (have == need):
                # update the result
                if (R - L + 1) < resLen:
                    resLen = (R - L + 1)
                    res = [L, R]
                
                window[s[L]] -= 1

                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                
                L += 1

        return s[res[0]: res[1] + 1] if resLen != float("inf") else ""


#Test Case

mySolution = Solution()

print("Test Case 1: ", mySolution.minWindow("ADOBECODEBANC", "ABC"))
print("Test Case 2: ", mySolution.minWindow("a", "a"))
print("Test Case 3: ", mySolution.minWindow("a", "aa"))
