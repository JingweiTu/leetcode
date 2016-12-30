class Solution(object):

    # Naive solution. O(nlogn) time. Linear space complexity. 
    # Pretty self-explanatory. 
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = 0
        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] > max_diff:
                max_diff = nums[i+1] - nums[i]
        return max_diff

    # Another naive solution. O(n) time. Linear space complexity.
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        max_diff = 0
        nums_set = set(nums)
        current_diff = 0
        for i in range (min_val, max_val+ 1):
            if not i in nums_set:
                current_diff += 1
            if i in nums_set:
                if current_diff > max_diff:
                    max_diff = current_diff
            
        return max_diff