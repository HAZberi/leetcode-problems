class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.cache = {}

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            if (j, root) in self.cache:
                return self.cache[(j, root)]
            
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.word
        
        return dfs(0, self.root)
    
#Test Case
myTrie = WordDictionary()
myTrie.addWord("bad")
myTrie.addWord("dad")
myTrie.addWord("mad")
myTrie.addWord("ape")
myTrie.addWord("ace")
print("Search 'pad':" ,myTrie.search("pad"))
print("Search 'bad':" ,myTrie.search("bad"))
print("Search '.ad':" ,myTrie.search(".ad"))
print("Search '.ad':" ,myTrie.search("b.."))
print("Search '.t.':" ,myTrie.search(".t."))
print("Search '.c.':" ,myTrie.search(".c."))
