class Solution(object):

    # Condensed solution.
    # O(n^2) time complexity. Linear time complexity.
    # Use b(number) to get a binary string representation of each hour and minute combination.
    # Combine each pair of strings and use count() to count number of 1s. 
    # If the number of 1s is equal to nums, append to the output list.
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # 02d means 2 digits.
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]