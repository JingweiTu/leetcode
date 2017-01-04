class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Keep track of the number of zeroes and remove them as they are enountered.
    # Append num_zeroes*[0] to the end of the now zero-less nums.
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        num_zeroes = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                i -= 1
                num_zeroes += 1
            i += 1
        nums += [0]*num_zeroes
            