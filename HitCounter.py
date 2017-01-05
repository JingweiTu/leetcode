
# O(n) time complexity. Linear space complexity.
class HitCounter(object):

    # Keep track of hits using a dictionary, where key = timestamp and value = number
    # of hits at that timestamp
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = {}
        
    # O(1) time complexity. Constant space complexity.
    # Populate self.counter with each hit.
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not timestamp in self.counter:
            self.counter[timestamp] = 1
        else:
            self.counter[timestamp] += 1

    # O(n) time complexity. Constant space complexity input. Linear space complexity function.
    # Cycle through dictionary, simultaneously removing timestamps from over 5 minutes 
    # (300 seconds) ago and summing the number of hits that fall into the acceptable bounds.
    # 
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        sum = 0
        for i in self.counter.keys():
            if i <= timestamp - 300:
                del self.counter[i]
            else:
                sum += self.counter[i] 
        return sum
            
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)