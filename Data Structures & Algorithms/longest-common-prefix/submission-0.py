class TrieNode:
    def __init__(self):
        # Maps a character to its TrieNode child
        self.children = {}
        # True if this node represents the end of an inserted string
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def find_longest_common_prefix(self) -> str:
        node = self.root
        prefix = []
        
        # Keep traversing as long as there is exactly 1 child 
        # and we haven't reached the end of the shortest word.
        while len(node.children) == 1 and not node.is_end_of_word:
            # Get the only character key in the children dictionary
            char = list(node.children.keys())[0]
            prefix.append(char)
            # Move to the child node
            node = node.children[char]
            
        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge cases
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
            
        trie = Trie()
        
        # Insert all words into the Trie
        for word in strs:
            # If there's an empty string, the longest common prefix is empty
            if word == "":
                return ""
            trie.insert(word)
            
        return trie.find_longest_common_prefix()