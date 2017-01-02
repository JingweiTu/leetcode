class Solution(object):

    # O(n) time complexity. Linear space complexity. 
    # Three cases:
    # Case 1: range is (i, i + 2). We append "i+1" to ans
    # Case 2: range is (i, i + x), where x > 2. We append ("i+1->i+x-1") to ans
    # Case 3: range is (i,i+1). We do nothing.
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        low = lower - 1
        nums.append(upper+1)
        for i in nums:
            if i == low + 2:
                ans.append(str(i-1))
            elif i > low + 2:
                ans.append(str(low + 1) + "->" + str(i-1))
            low = i
        return ans