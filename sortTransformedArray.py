class Solution(object):
    
    # O(nlogn) time complexity. Linear space complexity.
    # define a function fx to calculate ax^2 + bx + c more cleanly.
    # Use list comprehension to apply fx to every element of nums and sorted to sort it.
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def fx(x):
            return a*x**2 + b*x + c
        return sorted([fx(i) for i in nums])


# Optimized solution using bisect. 
# bisect.insort is O(n) and inserts into a sorted list, so there is no need 
# for a costly nlogn sort.
import bisect 
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        output = []
        def fx(x):
            return a*x**2 + b*x + c
        
        for i in nums:
            bisect.insort(output,fx(i))

        return output