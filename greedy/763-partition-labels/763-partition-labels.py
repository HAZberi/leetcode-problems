from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        partitionSize = 0
        endingIndex = 0
        for i, c in enumerate(s):
            partitionSize += 1
            endingIndex = max(endingIndex, lastIndex[c])

            if endingIndex == i:
                res.append(partitionSize)
                partitionSize = 0
        
        return res

#Test Case 
my_solution = Solution()
print("Test Case 1: ", my_solution.partitionLabels("ababcbacadefegdehijhklij"))
print("Test Case 2: ", my_solution.partitionLabels("eccbbbbdec"))