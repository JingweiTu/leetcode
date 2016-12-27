class Solution(object):

    # O(n) time. Linear space complexity. Run through the sorted array of citations.
    # If the ith index has a number of citations larger than or equal to N-i (the remaining)
    # number of citations, then we return N-i (the number of citations, including the ith) left over.
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        
        if N == 0:
            return 0
            
        citations.sort()
        
        for i in range(N):
            if (N - i) <= citations[i]:
                return N-i
        return 0
