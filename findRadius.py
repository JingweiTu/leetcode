class Solution(object):

    # Naive solution.
    # O(n^2) time complexity. Linear space complexity.
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = 1
        # distance from house to nearest heater
        dist = {}
        houses.sort()
        heaters.sort()
        for i in houses:
            for j in heaters:
                dist[i] = dist.get(i,abs(i-j))
                if abs(i-j) < dist[i]:
                    dist[i] = abs(i-j)
        return max(dist.values())

    # Using binary search. 
    def findRadius(self, houses, heaters):
    heaters.sort()
    return max(min(abs(house - heater)
                   for i in [bisect.bisect(heaters, house)]
                   for heater in heaters[i-(i>0):i+1])
                   for house in houses)
                
            
