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

    # O(n) time complexity. Linear space complexity. 
    # Because sets don't care about duplicates, if there is a duplicate, then it will not be 
    # counted twice in the set version of nums. Thus, if there is a duplicate, the length of 
    # nums as a list will be longer than nums as a set.
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(nums) != len(set(nums))