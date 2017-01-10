class Solution(object):

    # O(n)time complexity. Linear space complexity.
    # Append -inf to each end of nums. 
    # Search through elements of nums until we find nums[i] such that:
    # nums[i] > nums[i-1] and nums[i] > nums[i+1]
    # Return i-1.
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
            
        nums = [float("-inf")] + nums + [float("-inf")]
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i -1
        else:
            return -1
                
    # O(logn) time complexity. Linear space complexity.
    # Binary search. If the index to the right of the current is greater than the current,
    # search through the indices right of current. Otherwise, search through the left side.
    def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left+right)/2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid

        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid-1

    return left