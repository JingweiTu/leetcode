class Solution(object):

    # Iterative solution.
    # O(n) time complexity. Constant space complexity.
    # Keep dividing num by 4 as long as it is divisible by 4 and has a remainder of 0.
    # If num is a power of 4, the while loop should end with num == 1. Else, it is 
    # not divisible by 4.
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 4 and num%4 == 0:
            num = num/4 
        
        return num == 1