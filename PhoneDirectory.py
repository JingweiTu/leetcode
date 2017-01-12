class PhoneDirectory(object):

    # O(n) time complexity. Linear space complexity.
    # Keep two sets of numbers. Those that are free and those that are taken. 
    # The free set initially contains all the numbers from 0 to maxNumbers.
    # The taken set is initially empty.
    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.freeNumbers = set([i for i in range(maxNumbers)])
        self.takenNumbers = set()

    # Check there are any free numbers left. If so, pop it from the free set and 
    # add it to the taken set. Then return the number.
    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.freeNumbers) == 0:
            return -1
        else:
            newNumber = self.freeNumbers.pop()
            self.takenNumbers.add(newNumber)
            return newNumber
        
    # Check if number is in the free set.
    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.freeNumbers

    # Check if the number is in the taken set. If it is, remove it and add it to the 
    # free set.
    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number in self.takenNumbers:
            self.takenNumbers.remove(number)
            self.freeNumbers.add(number)
        
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)