# class TrieNode:
#     def __init__(self) -> None:
#         self.children = {}
#         self.end = False

# class WordDictionary:

#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         cur = self.root
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()            
#             cur = cur.children[c]

#         cur.end = True

#     def search(self, word: str) -> bool:
#         def dfs(j, root):
#             cur = root
#             for i in range(j, len(word)):
#                 c = word[i]
#                 if c == ".":
#                     for child in cur.children.values():
#                         if dfs(i+1, child):
#                             return True
#                     return False
#                 else:
#                     if c not in cur.children:
#                         return False
#                     cur = cur.children[c]
#             return cur.end
#         return dfs(0, self.root)

# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str):
        def dfs(word, node):
            for idx, ch in enumerate(word):
                if ch not in node:
                    if ch == '.':
                        for child in node:
                            if child != '$' and dfs(word[idx+1:], node[child]):
                                return True
                    return False
                else:
                    node = node[ch]

            
            return '$' in node
        return dfs(word, self.trie)

#         def search_in_node(word, node) -> bool:
#             for i, ch in enumerate(word):
#                 if ch not in node:
#                     # if the current character is '.'
#                     # check all possible nodes at this level
#                     if ch == '.':
#                         for x in node:
#                             if x != '$' and search_in_node(word[i + 1:], node[x]):
#                                 return True
#                     # if no nodes lead to answer
#                     # or the current character != '.'
#                     return False
#                 # if the character is found
#                 # go down to the next level in trie
#                 else:
#                     node = node[ch]
#             return '$' in node

#         return search_in_node(word, self.trie)


    




































