class Solution(object):

    # O(n) time complexity. Linear space complexity. 
    # This is bit manipulation.
    # The trick is to realize that any number XOR with itself is 0.
    # Any number XOR with 0 is itself, and XOR is commutative. 
    # Thus for nums = [a,b,c,d,a,b,c], we get (a^a)^(b^b)^(c^c)^d
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans = ans^i
        return ans