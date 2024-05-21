class Solution: #O(26)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1 = {}
        window = {}

        for s in s1:
            countS1[s] = 1 + countS1.get(s, 0)

        L = 0
        for R in range(len(s2)):          
            window[s2[R]] = 1 + window.get(s2[R], 0)

            if (R - L + 1) > len(s1) - 1:
                matches = 0
                for char in countS1:
                    if char in window and window[char] >= countS1.get(char, 0):
                        matches += 1
                
                if matches == len(countS1):
                    return True
                
                window[s2[L]] -= 1
                L += 1
        

        return False


class OptimizedSolution: #O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1 = [0] * 26
        countS2 = [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if countS1[i] == countS2[i] else 0)

        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[R]) - ord('a')
            countS2[index] += 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] + 1 == countS2[index]:
                matches -= 1

            index = ord(s2[L]) - ord('a')
            countS2[index] -= 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] - 1 == countS2[index]:
                matches -= 1
            
            L += 1
        
        return matches == 26


#Test Case
mySolution = Solution()
myOptimizedSolution = OptimizedSolution()

print(mySolution.checkInclusion("adc", "dcda"))
print(mySolution.checkInclusion("ab", "eidbaoio"))
print(mySolution.checkInclusion("abc", "bcaa"))
print(mySolution.checkInclusion("abb", "bbaa"))
print(mySolution.checkInclusion("ab", "bca"))
print(myOptimizedSolution.checkInclusion("adc", "dcda"))
print(myOptimizedSolution.checkInclusion("ab", "eidbaoio"))
print(myOptimizedSolution.checkInclusion("abc", "bcaa"))
print(myOptimizedSolution.checkInclusion("abb", "bbaa"))
print(myOptimizedSolution.checkInclusion("ab", "bca"))