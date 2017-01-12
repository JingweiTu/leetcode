class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Two cases:
    # Case 1: Index is Even
    # The value at i-1 and i+2 are both smaller than that at i.
    # Since we are working up consecutively from 0 to n-1, we can assume that 
    # the values from 0 to i-1 are correctly sorted. Thus, we consider i-1 and i.
    # If nums[i-1] <= nums[i], we do nothing.
    # If nums[i-1] > nums[i], then we swap the elements at i-1 and i. We know for sure
    # that this maintains the previous ordering, because we are guaranteed that
    # nums[i-2] >= nums[i-1]
    # Case 2: Index is Odd
    # The value at i-1 and i+2 are both larger than that at i.
    # Conceptually same as the even case. 
    # If nums[i-1] >= nums[i], we do nothing.
    # If nums[i-1] < nums[i], then we swap the elements at i-1 and i. 
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1,n):
            if (i % 2 == 0 and nums[i] > nums[i-1]) or (i % 2 == 1 and nums[i] < nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]