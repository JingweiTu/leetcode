class Solution(object):
    
    # The map(None, ...) transposes the "matrix", filling missing spots with None. For example:

    # ["abc",           [('a', 'd', 'f'),
    #  "de",     =>      ('b', 'e', None),
    #  "f"]              ('c', None, None)]
    # And then I just need to check whether transposing it once more changes it.

    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        t = map(None, *words)
        return t == map(None, *t)
        