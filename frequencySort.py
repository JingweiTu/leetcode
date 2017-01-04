import operator

class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Create char_dict, which keeps track of all the chars encountered and their frequencies.
    # Use sorted to sort chars by frequency and return them in an ordered pair as (char, freq)
    # for each char, in descending order of frequency, append n of that char to output, where
    # n == frequency.
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        char_dict = {}
        for c in s:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] +=1
                
        char_dict = sorted(char_dict.items(), key=operator.itemgetter(1))
        for i in range(len(char_dict) - 1, -1, -1):
            num, c = char_dict[i]
            output += num*c
        return output
