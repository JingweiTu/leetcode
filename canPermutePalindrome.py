class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Create a dictionary of chars. Cycle through all the characters in s.
    # The chars dictionary keeps track of how many times each char shows up.
    # If two chars show up in odd amounts, we instantly know there can be no palindrome.
    # Otherwise, return true.
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = {}
        for i in s:
            if not i in chars:
                chars[i] = 1
            else:
                chars[i] += 1
        num_odd = 0
        for i in chars.values():
            if i%2 == 1:
                num_odd += 1
                if num_odd > 1:
                    return False
        return True
                
