from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbours = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        
        visited = set()
        queue = deque()
        res = 1

        visited.add(beginWord)
        queue.append(beginWord)

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
                
            res += 1
        
        return 0
    
#Test Cases:
mySolution = Solution()
print("Test Case 1: ", mySolution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print("Test Case 2: ", mySolution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
