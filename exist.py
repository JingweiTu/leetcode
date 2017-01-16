from copy import copy

class Solution(object):

    # DFS time complexity is O(V + E). We run DFS on each index that starts with the same
    # letter as word. So time complexity of exist is O ((# of times the first letter of word
    # appears)* (length of word + 3*number of indices)). 
    # O(h) space complexity, where h is the max depth of the DFS recursion.
    # Run DFS on each index of the board that starts with the same letter as word.
    #
    # For future: Do not pass a visted_copy set between recursive steps. Implement this another
    # way.
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0]) 
        
        def dfs(row, col, remainder, visited):
            if remainder == "":
                return True
                
            if row >= 0 and col >=0 and row < rows and col < cols and board[row][col] == remainder[0] and (row,col) not in visited:
                visted_copy = copy(visited)
                visted_copy.add((row,col))
                return dfs(row - 1, col, remainder[1:], visted_copy) or dfs(row + 1, col, remainder[1:], visted_copy) or dfs(row, col - 1, remainder[1:], visted_copy) or dfs(row, col + 1, remainder[1:], visted_copy)
            else:
                return False
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, word, set()):
                        return True
        return False
