import heapq

class Solution(object):

    # O(nlogn)? Linear space complexity.
    # One line solution.
    # Use the * to indicate that lists within matrix are to be individually treated as merge
    # candidates. It makes matrix into a big tuple.
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return list(heapq.merge(*matrix))[k-1]

    