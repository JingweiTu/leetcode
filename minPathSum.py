class Solution(object):

    # O(mn) time. Linear space complexity. Dynamic programming solution. 
    # Essentially, we update the grid with based on whatever values are 
    # above and to the left of the current index (specifically, we set it 
    # to the sum of itself and the minimum of the left and upper indices).
    # The value of the minimum path is equal to that of the lower right index.
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range (m):
            for j in range(n):
                current = grid[i][j]
                if (i == 0 and not j == 0):
                    grid[i][j] += grid[i][j-1];
                if (not i == 0 and j == 0):
                    grid[i][j] += grid[i-1][j]
                if (not i == 0 and not j == 0):
                    grid[i][j] = min(grid[i-1][j] + current, grid[i][j-1] + current)
        return grid[m-1][n-1]
                