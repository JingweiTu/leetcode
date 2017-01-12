class Solution(object):

    # Can probably be improved.
    # O(n) time complexity. Linear space complexity.
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        output = []
        # Remove all dashes and capitalize all lowercase
        # We want to put off string concatenation as much as possible, as it is very costly, 
        # so we keep a list output that we will join at the very end.
        for i in S:
            if i != "-":
                if i.isalpha():
                    i = i.capitalize()
                output.append(i)
                
        # If there is going to be a short section in the beginning, we want to find
        # the index at which it ends. This is where we put our first "-"
        short_section_end_index = len(output)%K
        if short_section_end_index > 0:
            dash_index = short_section_end_index 
        else: 
            dash_index = K
        
        # Keep adding "-"
        while dash_index < len(output):
            output.insert(dash_index,"-")

            # increment by K+1, because the length of output increases, as well. When we insert
            # "-" at i, output[i] becomes "-" and everything after it is pushed forward by 1
            dash_index += K + 1
        
        return "".join(output)
            
            
