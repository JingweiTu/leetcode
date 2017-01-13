class Solution(object):]

    # O(n) time complexity. Linear space complexity.
    # Essentially, we are finding as much of an overlap between the reverse of s and s.
    # Once we do that, we can determine where to cut off the right side of reversed s 
    # and append it to s. Another way of looking at it is that we are finding the largest 
    # palindrome in s starting from the first index of s.
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(reverse[i:]):
                return reverse[:i] + s