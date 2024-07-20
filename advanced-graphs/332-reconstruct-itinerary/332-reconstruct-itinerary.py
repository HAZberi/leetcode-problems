from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = { src : [] for src, dst in tickets}

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = adj[src]
            for i, neighbour in enumerate(temp):
                adj[src].pop(i)
                res.append(neighbour)

                if dfs(neighbour): return True

                adj[src].insert(i, neighbour)
                res.pop()

            return False

        dfs("JFK")
        return res

#Test Case:
my_solution = Solution()
print("Test Case 1: ", my_solution.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print("Test Case 2: ", my_solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))



