class Solution(object):

    # O(n^2) time complexity. Linear space complexity.
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Create a list of "False" corresponding to each char in s.
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                # w == s[i-len(w)+1:i+1] means w can be constructed from s[i-len(w)+1:i+1]
                # d[i-len(w)] means that another word ended at the index before the start 
                # of this one
                # i-len(w) == -1 means we are looking at the first word in s (eg "leet" in
                # "leetcode")
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]