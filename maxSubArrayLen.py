class Solution(object):

    # O(n) solution. Linear space complexity.
    # Keep a dictionary of the accumulated sum of values of nums from i to len(nums) -1.
    # We want to find, given an accumulated sum up to a certain index (acc), if there is a 
    # corresponding sum of indices of nums (acc - k) in our dictionary.
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # answer and the accumulative value of nums
        ans, acc = 0, 0               
        #key is acc value, and value is the index
        accumulations = {0:-1}                 
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in accumulations:
                accumulations[acc] = i 
            if acc-k in accumulations:
                ans = max(ans, i-accumulations[acc-k])
        return ans
            
            