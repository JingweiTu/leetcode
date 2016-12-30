# O(n) time complexity. Linear space complexity. 
# Solution uses deques, which are double-ended queues.

import collections

class MovingAverage(object):
    
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.current_size = 0
        self.values = collections.deque()
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.current_size < self.size:
            self.values.append(val)
            self.current_size += 1
            return 1.0*sum(self.values)/len(self.values)
        else:
            self.values.append(val)
            self.values.popleft()
            return 1.0*sum(self.values)/len(self.values)
    

# Optimized version of previous solution. collections.deque has a maxlen parameter.

import collections

class MovingAverage(object):
    
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.values = collections.deque(maxlen = size)
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.values.append(val)
        return 1.0*sum(self.values)/len(self.values)