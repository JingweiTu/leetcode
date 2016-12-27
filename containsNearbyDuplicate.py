class Solution(object):
    # Naive solution. O(n^2) time. Constant space complexity.
    # We compare each index with the next k indices and see if
    # a duplicate appears.
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 1:
            return False
            
        for i in range(0, len(nums)):
            for j in range(1,k+1):
                if i + j >= len(nums):
                    break
                if nums[i] == nums[i+j]:
                    return True
        return False

    # Optimal solution. O(n) time. Linear space complexity. We create a 
    # lookup dictionary and update the dictionary with the latest encounter
    # of each value (key: value, value: index).
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dictionary = {}
        for i, v in enumerate(nums):
            if v in nums_dictionary and i - nums_dictionary[v] <= k:
                return True
            nums_dictionary[v] = i
        return False
        