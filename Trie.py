class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.children = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current_node = self.root
        for i in range(len(word)):
            
            if i == len(word) -1:
                current_letter = word[i] + "#"
            else:
                current_letter = word[i]
            
            if current_letter not in current_node.children:
                current_node.children[current_letter] = TrieNode()
                current_node.children[current_letter].val = current_letter
            current_node = current_node.children[current_letter]
        
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        
        for i in range(len(word)):

            if i == len(word) -1:
                current_letter = word[i] + "#"
            else:
                current_letter = word[i]
            
            if current_letter in current_node.children:
                
                current_node = current_node.children[current_letter]
            else:
                return False
                
        return True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        
        for i in range(len(prefix)):

            current_letter = prefix[i]
            if current_letter in current_node.children:
                current_node = current_node.children[current_letter]
            elif current_letter + "#" in current_node.children and i == len(prefix) - 1:
                return True
            else:
                return False
                
        return True
        
# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")