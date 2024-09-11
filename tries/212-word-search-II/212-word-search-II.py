from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
                return 
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)


#Test Cases
mysolution = Solution()
print("Test Case 1: ", mysolution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print("Test Case 2: ", mysolution.findWords([["a","b"],["c","d"]], ["abcb"]))
print("Test Case 3: ", mysolution.findWords([["a","c"],["t","e"]], ["app", "ace", "ate"]))
print("Test Case 4: ", mysolution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","p"],["i","f","l","v"]], ["oath","pea","eat","rain"]))




