class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # We start by reversing the digits list so we can sequentially move up the number
    # from least significant to most significant using a for loop. 
    # We then prepend onto our ans list the value of each index + carry, which keeps track
    # of anys 1s being carried over.
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []
        digits = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            val = (digits[i] + carry)%10
            ans.insert(0,val)
            if digits[i] + carry == 10:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            ans.insert(0,1)
        return ans