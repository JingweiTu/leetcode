class ValidWordAbbr(object):
    
    # O(n) time complexity. Linear space complexity.
    # Create a dictionary of sets. Each key is the abbreviation of a word and each 
    # corresponding value is a set of all the words in the parameter "dictionary"
    # that have the corresponding abbreviation. 
    # Two cases in choosing abbreviation. 
    # If the length of the word is 1 or 2, then ust let the abbreivation be that word.
    # Otherwise, the abbreviation is s[0] + str(len(s) - 2) + s[-1]
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrev_dict = {}
        for s in dictionary:
            if len(s) < 3:
                abbrev = s
            else:
                abbrev = s[0] + str(len(s) - 2) + s[-1]
            
            if abbrev not in self.abbrev_dict:
                self.abbrev_dict[abbrev] = set()
            self.abbrev_dict[abbrev].add(s)

        
    # O(1) time complexity. Constant space complexity.
    # We find the abbreviation for word using the same formula as before.
    # Three cases.
    # If the abbreviation is not in our abbreviation dictionary, then return True.
    # If the abbreviation is in the our dictionary and word is in the set corresponding to 
    # that abbreviation and there are no other strings in that set, then return True.
    # Otherwise, return False.
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            abbrev = word
        else:
            abbrev = word[0] + str(len(word) - 2) + word[-1]
        if not abbrev in self.abbrev_dict:
            return True
        elif word in self.abbrev_dict[abbrev] and len(self.abbrev_dict[abbrev]) == 1:
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")