class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}
        
    # O(1) time complexity. Constant space complexity. 
    # Check the messages dictionary to see if the value has been encountered already. 
    # If it has already been encountered and the time difference is < 10, then we return False.
    # Otherwise, we update the timestamp in the messages dictionary to the most recent one,
    # and we return true. We only update the dictionary if we return True (ie, we print)
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.messages and (timestamp - self.messages[message] < 10):
            return False
        else:
            self.messages[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)