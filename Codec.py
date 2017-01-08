class Codec:

    # O(n) time complexity. Linear space complexity.
    # Create a single string such that before each word is the length of the word + ":"
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join('%d:' % len(s) + s for s in strs)

    # O(n) time complexity. Linear space complexity.
    # Find all the instances of ":" and append the string to follow.
    # Increment counter i by the length of the word, which is indicated before the ":"
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))