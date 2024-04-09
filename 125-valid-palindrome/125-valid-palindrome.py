class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L , R = 0, len(s) - 1

        while L < R:
            while L < R and not self.isAlphaNumeric(s[L]):
                L += 1
            while L < R and not self.isAlphaNumeric(s[R]):
                R -= 1   
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1

        return True

    def isAlphaNumeric(self, c):
        return ((ord("a") <= ord(c) <= ord("z")) or 
                (ord("A") <= ord(c) <= ord("Z")) or 
                (ord("0") <= ord(c) <= ord("9")))
    

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.isPalindrome("A man, a plan, a canal: Panama"))
print("Test Case 2: ", mySolution.isPalindrome("race a car"))
print("Test Case 3: ", mySolution.isPalindrome(" "))