# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # O(length of intervals). Constant time complexity.
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(Interval(start, end))
        result += intervals[i:]
        return result