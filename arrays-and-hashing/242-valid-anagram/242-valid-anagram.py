class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False

        return True

#TestCases

mySolution = Solution()

print("Test Case 1:", mySolution.isAnagram("anagram", "nagaram"))
print("Test Case 2:", mySolution.isAnagram("rat", "car"))
