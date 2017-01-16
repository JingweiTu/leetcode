# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    
    # Conceptually. "An iterator shouldn't copy the entire data but just iterate over the original data structure."

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            nestedList, i = self.stack[-1]
            self.stack[-1][1] += 1
            return nestedList[i].getInteger()
        else:
            return False
             

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            nestedList, i = s[-1]
            # If we've reached an index i == len(stack), it means we've passed the end of the stack element and so we remove it from the stack. Conceptually, this means we've explored all the values in that element.
            if i == len(nestedList):
                s.pop()
            else:
                # We get the next element in the the last element of the stack. If it is an integer, we return True and break the loop. Otherwise, we increment the index counter within the last element of our stack. Finally, we append the new list (formerly the next element within the last element of s) to the stack and set its index counter to zero. The while loop continues.
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())