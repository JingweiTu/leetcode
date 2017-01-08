class Solution(object):

    # O(n^2) time complexity. Linear space complexity.
    # Use dynamic programming. The subproblem for n is the number of steps to n - j**2,
    # where j is any number such that j**2 <= i. By using dynamic programming, we don't
    # need to calculate the number of squares to get to a number m more than once, because
    # we store it in list dp. 
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            min_squares = float("inf")
            j = 1
            while (i - j**2 >= 0):
                min_squares = min(min_squares, dp[i - j**2] + 1)
                j += 1
            dp[i] = min_squares
        return dp[n]
