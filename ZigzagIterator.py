# Naive Solution.
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.current_v = 1
        self.current_index = 0
        self.v1 = v1
        self.v2 = v2
        
    # O(1) time complexity. Constant space complexity.
    # Different set of cases to consider when we are looking at v1 and v2 respectively.
    # Case v1: As long as self.current_v is v1 and the index we are visiting is not out of bounds
    # we should be able to go ahead and return the value at self.v1[self.current_index] 
    # We also decide whether we switch to v2 or continue traveling through v1 based on 
    def next(self):
        """
        :rtype: int
        """
        if len(self.v1) == 0:
            self.current_v = 2
            
        if self.current_v == 1 and self.current_index < len(self.v1):
            ans = self.v1[self.current_index]
            if self.current_index < len(self.v2):
                self.current_v = 2
            else: 
                self.current_index += 1
            return ans
        
        if self.current_v == 2 and self.current_index < len(self.v2):
            ans = self.v2[self.current_index]
            if self.current_index + 1 < len(self.v1):
                self.current_v = 1
            self.current_index += 1
            return ans


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.current_index < len(self.v1) or self.current_index < len(self.v2):
            return True 
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())