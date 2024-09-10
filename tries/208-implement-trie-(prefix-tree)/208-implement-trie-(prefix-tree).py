class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True

#Test Case
mytrie = Trie()
mytrie.insert("apple")
mytrie.insert("ape")
print("Search 'apple':", mytrie.search("apple"))
print("Search 'app':", mytrie.search("app"))
print("Starts With 'app':", mytrie.startsWith("app"))
print("Insert 'app':", mytrie.insert("app"))
print("Search 'app':", mytrie.search("app"))
print("Search 'ape':", mytrie.search("ape"))
print("Starts With 'p':", mytrie.startsWith("p"))



