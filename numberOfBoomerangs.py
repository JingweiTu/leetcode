class Solution(object):

    # O(n^2) Time complexity. Linear space complexity.
    # For each point, find the distance from that point to all other points and store the count
    # for each value into a dictionary dist_dict. The point p will serve as the center of the 
    # boomerang and for each distance d in dist_dict, there are d*(d-1) possible boomerangs.
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        output = 0

        def getDist_Squared(i,j):
            return (i[0] - j[0])**2 + (i[1] - j[1])**2

        for p in points:
            dist_dict = {}
            for q in points:
                dist_squared = getDist_Squared(p,q)
                dist_dict[dist_squared] = 1 + dist_dict.get(dist_squared,0)
            for k in dist_dict:
                output += dist_dict[k] * (dist_dict[k] - 1)
        return output