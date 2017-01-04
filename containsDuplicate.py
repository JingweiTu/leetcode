class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Keep track of encountered numbers in nums_set. Cycle through nums. If value is not in 
    # nums_set, add it to nums_set. Otherwise, we have hit a duplicate and return True.
    # If we finish the loop without hitting a duplicate, we return False.
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set()
        for i in nums:
            if not i in nums_set:
                nums_set.add(i)
            else: 
                return True
        return False