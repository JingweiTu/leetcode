class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        rows = len(board)
        cols = len(board[0])
        
        # Depth first search of the matrix. We pass in trie, which is initially the root of all the words.
        # If we encounter a '#', we append the path to res (ie '#' indicates the end of a word, so the current path has created a word). 
        def find(board, i, j, trie, path, res):
            if '#' in trie:
                res.add(path)
        # If the row and col are not accessible or the letter at the current index is not in the trie, we end.
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j] not in trie:
                return
        # We set a temporary variable equal to the letter at the current index.
            tmp = board[i][j]
        # We set the current index to "@", indicating that we have already visited it.
            board[i][j] ="@"
        # We continue the DFS.
            find(board, i+1, j, trie[tmp], path+tmp, res)
            find(board, i, j+1, trie[tmp], path+tmp, res)
            find(board, i-1, j, trie[tmp], path+tmp, res)
            find(board, i, j-1, trie[tmp], path+tmp, res)
        # We set the board index back to what it was originally.
            board[i][j] = tmp
            
        # Build the Prefix tree. Add key '#' to the end of each word.
        trie = {}
        for w in words:
            node = trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = '#'
            
        res = set()
        # Run the DFS for each index in the board. We start with a path of "".
        for i in range(rows):
            for j in range(cols):
                find(board, i, j, trie, '', res)
        return list(set(res))
    
