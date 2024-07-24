from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #Building an adjacency list
        adj = { c:set() for w in words for c in w } #nested 
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        #Topological sort set up
        visited = {} # { char: False if visited, True if currently on the path }
        res = [] #sorted output in reverse order

        #Post Order DFS
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            res.append(c)
            visited[c] = False
        
        #Running dfs on each node of the graph
        for c in adj:
            if dfs(c):
                return ""
        
        #Reversing the output order
        res.reverse()
        return "".join(res)

#Test Cases
my_solution = Solution()
print("Test Case 1: ", my_solution.alienOrder(["z","o"]))
print("Test Case 2: ", my_solution.alienOrder(["hrn","hrf","er","enn","rfnn"]))


