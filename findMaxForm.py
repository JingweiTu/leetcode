class Solution(object):

    # O(n^3). 
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in xrange(m+1)]
        for s in strs:
            z,o = s.count('0'),s.count('1')
            for i in xrange(m,-1,-1):
                for j in xrange(n,-1,-1):                    
                    if z <= i and o <= j:
                        dp[i][j] = max(dp[i][j],1+dp[i-z][j-o])
        return dp[m][n]
            
