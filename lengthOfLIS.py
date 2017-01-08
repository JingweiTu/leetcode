class Solution(object):

    # O(n^2) time complexity. Linear space complexity.
    # Create a list of counters corresponding to the indices of nums and set each value to 1.
    # This is because the shortest possible sequence at any point is 1.
    # Cycle through nums with 2 pointers. i points to the value in nums and j will the all the
    # values before nums that may potentially be the previous index in the sequence leading up
    # to i. Update counters[i] with each value of j. If nums[j] < nums[i] and
    # 1 + counter[j] > counter[i], then let counter[i] = counter[j] + 1. Essentially, this 
    # means that counter[j] was the last index of the optimal (longest) sequence leading
    # up to nums[i]. 
    # Cycle through all of nums and return the highest value in counter. 
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        counters = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    counters[i] = max(1 + counters[j], counters[i])
        
        output = max(counters)
        return output