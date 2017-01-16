class Solution(object):

    # O(rows*cols + # of 1s) time complexity. O(h) space complexity, where h is recursion depth
    # Search through all the indices and run a BFS whenever we encounter a 1. The BFS sets any
    # vertical or horizontal 1s to -1, so we don't double count. We then increment island_count
    # by 1.
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        
        island_count = 0
        
        def BFS(row, col):
            if grid[row][col] == "1":
                grid[row][col] = "-1"
                directions = set([(row-1,col),(row+1,col),(row,col-1), (row,col+1)])
                for i,j in directions:
                        if 0 <= i < rows and 0 <= j < cols:
                            BFS(i,j)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    BFS(row,col)
        
        return island_count
                    
        