class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Keep track of  a running product (p) of the values of nums and set output[i] == the product 
    # of all values before it (ie p) during first loop. 
    # On the second loop, we work backwards, and keep a running product p of the values of nums
    # in reverse. Multiply each index of output by p, to get all the values before it.
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        for i in range(len(nums)):
            output.append(p)
            p = p*nums[i]
        p = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i] * p
            p = p *nums[i]
        return output
