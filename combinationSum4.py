class Solution(object):

    # O(n^2) time complexity. Linear space complexity.
    # Use Dynamic Programming
    # We start by sorting nums.
    # We then create an array representing all the numbers from 0 through target
    # We then seek to find the number of potential combinations of nums we can use to 
    # create each number from 0 through target.
    # There are 3 cases for each num in nums.
    # if num > i, we stop.
    # If i is in nums (ie num == i), we we increment that index in combs by 1.
    # If num < i, we find how many combinations make up i - num. Because i - num has 
    # already been explored, we know that it already contains the maximum number of
    # possible combinations of nums. eg if the current num were 2, and i == 5, we know 
    # that there are 4 ways to get to i-num == 3. Thus, there are 3 ways to make up the 
    # complement of num (3).
    # combs[target] will be the number of combinations to reach target.
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, combs = sorted(nums),  [0] * (target+1)
        for i in range(1,target + 1):
            for num in nums:
                if num > i: 
                    break
                if num == i: 
                    combs[i] += 1
                if num < i: 
                    combs[i] += combs[i - num]
        return combs[target]
