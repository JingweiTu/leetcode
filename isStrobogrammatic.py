class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # 4 cases. 
    # Case 1: unflippable numbers: ["2","3","4","5","7"]. If we encounter any of these, we
    # return False
    # Case 2: "6". If the number that takes its spot when num is flipped is 9 
    # (ie if num_string[len(num_string) - 1 - i] != "9") then we are okay. Otherwise, False.
    # Case 3: "9". Similar to 6 case.
    # Case 4: Similar to 6 and 9 case, except it has to be the same number in the corresponding
    # position. 
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_string = str(num)
        bad_numbers = set(["2","3","4","5","7"])
        for i in range(len(num_string)):
            if num_string[i] in bad_numbers:
                return False
            elif num_string[i] == "6":
                if num_string[len(num_string) - 1 - i] != "9":
                    return False
            elif num_string[i] == "9":
                if num_string[len(num_string) - 1 - i] != "6":
                    return False
            elif num_string[len(num_string) - 1 - i] != num_string[i]:
                return False
        return True
