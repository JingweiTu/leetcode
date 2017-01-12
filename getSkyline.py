import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # Get a sorted list of (L, -H, R) combined with (R,0,0)
        p = sorted([(L, -H, R) for L, R, H in buildings] + list(set((R, 0, 0) for L, R, H in buildings)))
        ret, heap = [], []
        for L, negH, R in p:
            # As long as the heap is not empty and L (the left index) is greater than R (
            # the right index) of the min element in the heap, we remove the min element. 
            # Essentially, we are disregarding the values in the heap to the left of L 
            # and keeping all the buildings that have right sides past L.
            while heap and L >= heap[0][1]:
                heapq.heappop(heap)
            # Add the negative value of the height (negH) and R to the min heap. 
            # This ensures that the tallest building stays at the top of the heap.
            heapq.heappush(heap, (negH, R))
            # If ret is empty or the height of the last value in ret is not equal to 
            # the negative of the min value in the heap, append (L, -H) to ret. 
            if not ret or ret[-1][1] != -heap[0][0]: 
                ret.append([L, -heap[0][0]])
        return ret