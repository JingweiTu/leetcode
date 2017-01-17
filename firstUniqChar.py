import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1 
            
        dic = collections.OrderedDict()
        for i in s:
            dic[i] = dic.get(i,0)
            dic[i] += 1
        

        num = 0
        while num != 1 and len(dic) > 0:
            char, num = dic.popitem(last=False)
            if num == 1:
                return s.find(char)
            
        return -1