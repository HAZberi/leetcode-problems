class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0, 0] #will store the [l, r] pointers
        resLen = 0

        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) >= resLen:
                    resLen = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1

            #even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) >= resLen:
                    resLen = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1
        
        return s[res[0]:res[1] + 1]

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.longestPalindrome("babad"))
print("Test Case 2: ", my_solution.longestPalindrome("cbbd"))

