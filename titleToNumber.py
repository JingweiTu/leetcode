class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # We work backwards through the string s, so we reverse it as s[::-1]
    # Then, we know each character in s corresponds to an increasing exponent of 26, which
    # we keep track of through the variable n. Finally, to get the numerical value of each 
    # letter, we note that the ASCII values of each letter is sequential, and that A == 65.
    # Thus, we subtract 64 from the ASCII value of each letter to get the value we want, and
    # then we multiply it by the corresponding exponent of 26.
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        output = 0
        for c in s[::-1]:
            output += (ord(c) - 64)*(26**n)
            n +=1
        return output