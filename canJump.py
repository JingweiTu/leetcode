class Solution(object):
    # O(n) time. Constant space complexity. The concept is that we keep track of 
    # the maximum reachable index at each iterative step. If the next index 
    # is further away than the current maximum reachable index, then we return false.
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            else:
                max_reachable = max(max_reachable, nums[i] + i)
        return True
            
