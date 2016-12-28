
class Solution(object):

    # Naive solution. O(N^2) time complexity. Lineary space complexity. Loop through all
    # possible combinations of values. 
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(height) -1):
            for j in range (i+1, len(height)):
                volume = (j-i)*(min(height[j],height[i]))
                if  volume > ans:
                    ans = volume
        return ans

        # O(n) time complexity. Linear space complexity. We begin by finding the volume
        # of the widest container. We then shrink the container in such a way that we 
        # always keep the higher wall and close in towards the middle. 
        def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water