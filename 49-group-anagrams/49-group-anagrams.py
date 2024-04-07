class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {} #mapping char counts to the list of anagrams

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1
                
            count = tuple(count)
            if count in res:
                res[count].append(s)
            else:
                res[count] = [s]
            
        return list(res.values())

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print("Test Case 2: ", mySolution.groupAnagrams([""]))
print("Test Case 3: ", mySolution.groupAnagrams(["a"]))


