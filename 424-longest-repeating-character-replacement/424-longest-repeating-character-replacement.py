class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        L = 0
        longest = 0

        for R in range(len(s)):
            charCount[s[R]] = 1 + charCount.get(s[R], 0)

            while (R - L + 1) - max(charCount.values()) > k:
                charCount[s[L]] -= 1
                L += 1
            longest = max(longest, R - L + 1)
        
        return longest

class OptimizedSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        L = 0
        longest = 0
        maxf = 0

        for R in range(len(s)):
            charCount[s[R]] = 1 + charCount.get(s[R], 0)
            maxf = max(maxf, charCount[s[R]])

            while (R - L + 1) - maxf > k:
                charCount[s[L]] -= 1
                L += 1
            longest = max(longest, R - L + 1)
        
        return longest


#Test Cases

mySolution = Solution()
myOptimizedSolution = OptimizedSolution()

print("Test Case 1: ", mySolution.characterReplacement("ABAB", 2))
print("Test Case 2: ", mySolution.characterReplacement("AABABBA", 1))
print("Test Case 3: ", mySolution.characterReplacement("AABABBA", 2))
print("Test Case 1: ", myOptimizedSolution.characterReplacement("ABAB", 2))
print("Test Case 2: ", myOptimizedSolution.characterReplacement("AABABBA", 1))
print("Test Case 3: ", myOptimizedSolution.characterReplacement("AABABBA", 2))