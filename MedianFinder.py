# Naive solution. 

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.values = []
        
    # O(1) time complexity. Constant space complexity.
    # Appends num to unsorted list.
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.length += 1
        self.values.append(num)
        

    # O(n) time complexity. Constant space complexity.
    # Sort the values in self.values. Find median.
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        self.values.sort()
        if self.length%2 ==0:
            return (self.values[self.length//2 - 1] + self.values[self.length//2])/2.0
        else:
            return self.values[self.length//2] 

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()


import bisect 

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.values = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.length += 1
        bisect.insort(self.values, num)
        
            

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.length%2 ==0:
            return (self.values[self.length//2 - 1] + self.values[self.length//2])/2.0
        else:
            return self.values[self.length//2] 

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()