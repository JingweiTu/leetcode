class Solution(object):
    # O(n) time. Linear time complexity. We divide by 2 (pop the last bit) and see if the last
    # bit is 1. 
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans += n%2
            n = n/2
        return ans
