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
            
            if (R - L + 1) > len(s1):
                matches = 0
                for char in window:
                    if char not in countS1 and window[char] != countS1.get(char, 0):
                        break
                    else:
                        matches += 1
                
                if matches == len(countS1):
                    return True
                if window[s2[L]] > 1:
                    window[s2[L]] -= 1
                else:
                    del window[s2[L]]
                L += 1
        
        return False


#Test Case
mySolution = Solution()

print(mySolution.checkInclusion("adc", "dcda"))
print(mySolution.checkInclusion("ab", "eidboaio"))
print(mySolution.checkInclusion("abc", "bcaa"))
print(mySolution.checkInclusion("abb", "bbaa"))