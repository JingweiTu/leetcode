class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        gmax, cols = 0, [0] * len(grid[0])
        
        for row in xrange(len(grid)):
            rowhits = 0
            for col in xrange(len(grid[0])):
                if (col ==0 or grid[row][col-1] == 'W'):
                    rowhits = 0;
                    for k in xrange(col,len(grid[0])):
                        if grid[row][k] == 'W':
                            break
                        rowhits = rowhits + 1 if grid[row][k] == 'E' else rowhits
    
                if row == 0 or grid[row-1][col] == 'W':
                    cols[col] = 0
                    for k in xrange(row,len(grid)):
                        if grid[k][col] == 'W':
                            break
                        cols[col] = cols[col] + 1 if grid[k][col] == 'E' else cols[col]
    
                    
                if grid[row][col] == '0':
                    gmax = max(gmax, rowhits + cols[col])
        
        return gmax
                    