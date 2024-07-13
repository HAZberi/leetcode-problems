class Solution:
    def countSubstringsV1(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l, r = i, i #odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l, r = i, i + 1 #even length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

#Test Case:
my_solution_v1 = Solution()
print("Test Case 1: ", my_solution_v1.countSubstringsV1("abc"))
print("Test Case 2: ", my_solution_v1.countSubstringsV1("aaa"))

class SolutionV2:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPalindromes(s, i, i)
            res += self.countPalindromes(s, i, i + 1)

        return res
    
    def countPalindromes(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        return res

#Test Case:
my_solution_v2 = SolutionV2()
print("Test Case 1: ", my_solution_v2.countSubstrings("abc"))
print("Test Case 2: ", my_solution_v2.countSubstrings("aaa"))
