class Solution(object):
    # O(n) time complexity. Constant space complexity.
    # This is bit manipulation with Dynamic Programming. 
    # The main point is that we want as few 1s in our binary representation as possible,
    # because with every division by 2, we shift over to the right by one value. If the 
    # rightmost bit is a 1, we need to subtract 1 first, in order to divide evenly (as per 
    # instructions). Thus, it takes two steps to remove a 1 and one step to remove a 0. 
    # Any multiple of 4 can be represented by the bit string b'1...00'. Thus, if
    # n is 1 more than a multiple of 4, it can be represented as b'1...01', so subtracting 1 
    # removes a 1 from the string while adding a 1 doesn't change the number of 1s.
    # However, a value that is not even or not one more than a mutiple of 4, the number can
    # only be represented by b'1...11'. Adding one in this case turns at least twos 1s into 0s.
    
    # We are told to divide n by 2 if n is even. Otherwise, we consider two cases.
    # If n % 4 == 1, we know that n can be represented as b'1...01'. We want to reduce by 1 to
    # have b'1...00', which will definitely be divisible by 2. 
    # If n == 3, n == b'11', subtracting 1 will give us 2, which is one division step away from 1.

    # 

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn