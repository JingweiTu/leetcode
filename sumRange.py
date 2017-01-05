# Naive solution. Might be faster if implemented with lists.
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = {}
        for i,v in enumerate(nums):
            self.nums[i] = v

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = 0
        for x in range(i,j+1):
            sum += self.nums[x]
        return sum


# Optimal solution.
# We note that if we replace each index with the sum of all the previous index,
# the sum from index i to j of the original nums list, inclusive, will be the difference of 
# index j + 1 and i in our new list, self.accu.
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for i in range(len(nums)): 
            self.accu.append(nums[i] + self.accu[i])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        return self.accu[j + 1] - self.accu[i]

