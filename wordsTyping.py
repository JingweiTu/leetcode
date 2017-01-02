class Solution(object):

    # Naive solution. O(n^2) time complexity. Linear space complexity.
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        counter = 0
        word_lengths = [len(x) for x in sentence]
        sentence_index = 0
        for i in range(rows):
            num_spaces = cols
            while num_spaces > 0:
                num_spaces -= word_lengths[sentence_index] +1
                
                if num_spaces >= -1:
                    sentence_index += 1
                    if sentence_index == len(word_lengths):
                        sentence_index = 0
                        counter += 1
                
        return counter