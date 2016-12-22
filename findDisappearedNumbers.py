class Solution(object):

	# naive solution. O(n^2) time. Constant space. 
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                ans.append(i)
        return ans
	
	# O(n) time. Linear space.
    def findDisappearedNumbers_LS(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # create list with all numbers in range [1, nums+1]
        all_nums = list(range(1, len(nums) + 1))
        #create a list that returns all values in all_nums but not nums
        ans = [x for x in all_nums if x not in nums]
        return ans

    #One-liner.
    # Use sets to speed up lookup. Sets are significantly faster when it comes to determining if an object is present in the set (as in x in s), but are slower than lists when it comes to iterating over their contents.
    class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))
            
        