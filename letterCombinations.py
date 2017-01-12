class Solution(object):

    # Ask about time complexity for this one.
    # Keep a dictionary of letters corresponding to each number.
    # Recursively build the strings. 
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_to_letters = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        
        output = []
        def recurse(digits, index, s, output):
            if len(digits) == 0:
                return
            if len(s) == len(digits):
                output.append(s)
            else:
                for char in num_to_letters[digits[index]]:
                    recurse(digits, index+1, s+char, output)
        
        recurse(digits, 0, "", output)
        return output
                    
                

        