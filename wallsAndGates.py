class Solution(object):

    # O() time complexity. Linear space complexity.
    # Recursive solution using DFS. 
    # We run the recursion once we hit a 0.
    # If all the cases fail for DFS to continue, we return.
    # Otherwise, we keep running the DFS on the 4 ordinal coordinates.
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0:
            return 
        
        numRows = len(rooms)
        numCols = len(rooms[0])
        def dfs(row,col,path_length):
            if (row < 0 or row >= numRows or col < 0 or col >= numCols or rooms[row][col] < path_length):
                return
            else:
                rooms[row][col] = path_length
                dfs(row-1, col, path_length + 1)
                dfs(row+1, col, path_length + 1)
                dfs(row, col-1, path_length + 1)
                dfs(row, col+1, path_length + 1)
                    
                    
        for row in range(numRows):
            for col in range(numCols):
                if rooms[row][col] == 0:
                    dfs(row, col, 0)
