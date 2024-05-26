from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for letter in digitToLetters[digits[i]]:
                backtrack(i + 1, curStr + letter)
        
        if digits:
            backtrack(0, "")
        
        return res

#Test Cases:
mySolution = Solution()
print("Test Cases 1: ", mySolution.letterCombinations("23"))
print("Test Cases 2: ", mySolution.letterCombinations(""))
print("Test Cases 3: ", mySolution.letterCombinations("2"))
print("Test Cases 4: ", mySolution.letterCombinations("975"))