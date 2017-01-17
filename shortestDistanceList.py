class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        one_locations = set()
        two_locations = set()
        for i in range(len(words)):
            if words[i] == word1:
                one_locations.add(i)
            if words[i] == word2:
                two_locations.add(i)
            
        return min([abs(i - j) for i in one_locations for j in two_locations])