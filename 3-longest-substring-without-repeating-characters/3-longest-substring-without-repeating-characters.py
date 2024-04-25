class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        longest = 0

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            longest = max(longest, R - L + 1)

        return longest

#Test Cases
mySolution = Solution()

print("Test Cases 1: ", mySolution.lengthOfLongestSubstring("abcabcbb"))
print("Test Cases 2: ", mySolution.lengthOfLongestSubstring("bbbbb"))
print("Test Cases 3: ", mySolution.lengthOfLongestSubstring("pwwkew"))