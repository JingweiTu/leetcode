class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Keep a dictionary of characters that keeps track of the frequency of each character in s.
    # Since we want this to be case-sensitive, we use the ASCII value of each character as keys
    # since that distinguishes between cases. 
    # In the second loop, we go through all the values in char_dict. If the value is even, we
    # can use all of those chars. If it is odd, we can use val -1 of those chars. We make a 
    # note if we encounter any odd values as extra_odd.
    # Since the middle value of a palindrome can be anything, we can use one set of chars that
    # was odd in count. This is why we kept track of extra_odd. We sum sum_evens, sum_odds, and
    # extra_odd to get our final solution.
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_evens = 0
        sum_odds = 0
        extra_odd = 0
        char_dict = {}
        for i in s:
            if ord(i) not in char_dict:
                char_dict[ord(i)] = 1
            else:
                char_dict[ord(i)] += 1
        for val in char_dict.values():
            if val%2 == 0:
                sum_evens += val
            else:
                extra_odd = 1
                sum_odds += val - 1
        
        max_length = sum_evens + sum_odds + extra_odd
            
        return max_length