class Solution(object):
    # O(n) time complexity. Linear space complexity.
    # travel through all indices in the s. If we encounter two consecutive "+",
    # we build a string with those two "+" replaced with "-" and append this to ans.
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        s_list = list(s)
        for i in range(len(s)-1):
            if s[i] == "+" and s[i+1] == "+":
                ans.append(str(str("".join(s_list[0:i])) + "--" + str("".join(s_list[i+2:len(s)]))))
        return ans