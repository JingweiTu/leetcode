class Solution(object):

    # The concept is that we use dynamic programming to keep track of the longest set of 
    # values such that for any two values A and B, A% B ==0, for every index in nums.sort().
    # Essentially, we keep a list of lists dp[][] such that dp[i] is the maximum possible
    # combination of values in nums[0:i] such that for any two values A and B, A% B ==0. 
    # With each successive value of i, we take into consideration one more value of nums, and
    # we find the largest set from dp[0:i] that can include nums[i]. This could be []. 
    # Regardless, we append nums[i] to the max set for index i, and set dp[i] equal to it.
    # At the end, we return the largest set in dp.
    # https://discuss.leetcode.com/topic/49528/python-dp-n-2-solution
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        if n == 0:
            return []
            
        dp = [0] * n
        dp[0] = [nums[0]]
        #print(dp)
        for i in range(1, n):
            curNum = nums[i]
            maxSet = []
            for j in range(i):
                if curNum % nums[j] == 0:
                    localSet = list(dp[j])
                    if len(localSet) > len(maxSet):
                        maxSet = localSet
            
            maxSet.append(nums[i])
            dp[i] = maxSet
            #print(dp)
        
        print(dp)
        res = []
        for localSet in dp:
            if len(localSet) > len(res):
                res = localSet
        return res