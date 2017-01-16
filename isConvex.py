class Solution(object):
    
    # get the cross product of the sequential input edge a, b as tmp, then:
    # if tmp == 0, a -> b 180° on the same line
    # elif tmp > 0, a -> b clockwise
    # else tmp < 0, a -> anticlockwise
    # https://discuss.leetcode.com/topic/70643/i-believe-this-time-it-s-far-beyond-my-ability-to-get-a-good-grade-of-the-contest/10
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        last, tmp = 0, 0
        for i in range(2, len(points) + 3):
            p0, p1, p2 = points[(i - 2) % len(points)], points[(i - 1) % len(points)], points[i % len(points)]
            tmp = (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
            if tmp:
                if last * tmp < 0:
                    return False
                last = tmp
        return True