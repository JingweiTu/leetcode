class Solution(object):

    # O(n) time complexity. Constant space complexity.
    # There are 4 cases.
    # Case 1: Trivial case. There is no fence. Return 0.
    # Case 2: The fence is one post. There are k possibilities in this case.
    # Case 3: The fence is two posts long. If they are the same color, then the fence has 
    # k possible configurations. If they are different colors, then there are k*(k-1) configs.
    # Case 4: For fences with 3 or more posts, we consider the following.
    # If the next post is the same color as the previous post, then we multiply by 1 (we don't
    # add any new possible configs). We know we can set the variable same to equal that of dif,
    # which is the number of total configs if the previous post was differently colored from
    # the post before it. We also know that this is always true, since no 3 posts are alike,
    # so if a post is color x, the post before it's immediate previous post is definitely
    # different. 
    # If the next post is a different color from the last, then there are (k-1) possibilities.
    # We know that the total number of possibilities leading up to and including the
    # last post is (same + dif), ie the number of combinations given that the last post is the
    # same as its previous plus the number of combinations if it were different. Thus, dif
    # now equals (same + dif)(k+1)
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        dif = k*(k - 1)
        for i in range(3,n+1):
            same, dif = dif, (same+dif)*(k-1)
        return same + dif