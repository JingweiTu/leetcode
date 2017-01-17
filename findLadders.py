import collections
import string
def findLadders(beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordlist.add(endWord)
        # we're doing a level-order BFS
        level = {beginWord}
        # create a dictionary of sets representing the parents of the each word.
        parents = collections.defaultdict(set)
        
        while level and endWord not in parents:
            # create a dictionary of sets representing the next level
            next_level = collections.defaultdict(set)
            
            # check all the nodes in this level.
            for node in level:
                # check all potential characters that can be at index i
                for char in string.ascii_lowercase:
                    # insert char into every possible index from 0 to len(beginWord)
                    for i in range(len(beginWord)):
                        # create a new word from the previous word and the new char.
                        new_word = node[:i]+char+node[i+1:]
                        if new_word in wordlist and new_word not in parents:
                            next_level[new_word].add(node)
            level = next_level
            # append values from level into parent, indicating that we have visited them all.
            # ie parents['cog']: {'log'} becomes parents['cog']: {'log', 'dog'} after update.
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            # for each list in res, we add the parent of the first value in the list.
            # ie if ['cog'] is in res, we find that its parents are 'dog' and 'log', and we 
            # create separate lists given each option.
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res
                