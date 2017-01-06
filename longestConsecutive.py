import bisect 

class Solution(object):

    # 
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        sorted_nums = []
        nums_set = set(nums)
        while len(nums_set) > 0:
            bisect.insort(sorted_nums, nums_set.pop())
            
        longest_chain = 0
        current_chain = 0
        for i in range(len(sorted_nums)):
            if i+ 1 == len(sorted_nums) or sorted_nums[i] + 1 == sorted_nums[i + 1]:
                current_chain += 1
            else:
                current_chain += 1
                if current_chain > longest_chain:
                    longest_chain = current_chain
                current_chain = 0
                
        if current_chain > longest_chain:
            longest_chain = current_chain
        

        return longest_chain

                