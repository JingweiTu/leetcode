class Solution(object):
    # O(n) time complexity. Linear space complexity. Constant auxiliary space complexity.
    # This is really just a reading comprehension problem. There is no logic involved.
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        bitCount = 0;
    
        for n in data:
            
            if(n >= 192):
                if(bitCount != 0):
                    return False
                elif(n >= 240):
                    bitCount = 3
                elif(n >= 224):
                    bitCount = 2
                else:
                    bitCount = 1
            elif(n >= 128):
                bitCount -= 1
                if(bitCount < 0):
                    return False
            elif(bitCount > 0):
                return False
        
        
        return bitCount == 0;