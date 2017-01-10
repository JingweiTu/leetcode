import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys = collections.deque()
        self.cache = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.keys:
            self.cache[key] = value
            self.keys.remove(key)
            self.keys.append(key)
        elif len(self.keys) < self.capacity:
            self.keys.append(key)
            self.cache[key] = value
        else:
            LRU = self.keys.popleft()
            del self.cache[LRU]
            self.keys.append(key)
            self.cache[key] = value


import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return self.cache[key]
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value
            
            
            
            
        
            
        