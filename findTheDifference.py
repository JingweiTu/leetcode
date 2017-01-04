class Solution(object):
    # O(n) time complexity. Linear space complexity.
    # Make t into a list. Then remove each letter of s from t. The remaining value in t
    # is the difference.
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = list(t)
        for i in s:
            t.remove(i)
        return t[0]