class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Simply keep a stack of "left symbols" 
    # If a "right symbol" check to see if it matches the corresponding left symbol that is
    # at the top of the stack. If not, return False. If we have an empty stack, then return
    # False as well. If at the end of the loop we still have values in the stack,
    # also return False. Otherwise, return True.
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left_symbols = set(["(","{","["])
        right_symbols = set([")","}","]"])
        for i in s:
            if i in left_symbols:
                stack.append(i)
            if i in right_symbols:
                if len(stack) == 0:
                    return False 
                left = stack.pop()
                if not ((left == "(" and i == ")") or (left == "[" and i == "]") or (left == "{" and i == "}")):
                    return False
        return len(stack) == 0
        