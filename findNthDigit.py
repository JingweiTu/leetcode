class Solution(object):

    # Naive Solution
    # O(n) time complexity. Constant space complexity.
    # Keep a running sum of all the previous values' lengths. While sum_prev < n:
    # we add the length of the next consecutive number. When we reach a point where
    # the next consecutive number contains the nth digit, we return the digit at index n. 
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_prev = 0
        i = 1
        while sum_prev + len(str(i)) < n:
            sum_prev += len(str(i))
            i += 1        
        return int(str(i)[n - sum_prev - 1])

    # O(n) time complexity. Constant space complexity.
    # 
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size, step = 1, 1, 9
        while n > size * step:
            n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])