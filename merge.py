# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # O(n) time complexity. Linear space complexity.
    # Sort the each interval i from the list "intervals" by i.start. For each interval i, 
    # if output is not empty i.start is before the end of the last interval added to output
    # we set the end of the last value in output to equal the max of output[-1].end and i.end
    # Otherwise, we add the current interval, i, to the end of our output list.
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        output = []
        for i in sorted(intervals, key=lambda i: i.start):
            if len(output) > 0 and i.start <= output[-1].end:
                output[-1].end = max(output[-1].end, i.end)
            else:
                output += i,
        return output
            
            
            
            