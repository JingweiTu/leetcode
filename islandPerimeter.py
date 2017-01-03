class Solution(object):

    # Naive Solution. 
    # O(n^2) time complexity. Quadratic space complexity.
    # Add padding of 0s to the sides of the grid.
    # Cycle through the part of the new grid that constituted the old grid.
    # If the index == 1, we check how many sides are 0. Every side that faces a 0
    # will increase perimeter by 1.
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        grid.insert(0,[0]*len(grid[0]))
        grid.append([0]*len(grid[0]))
        for g in grid:
            g.insert(0,0)
            g.append(0)
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == 1:
                    if grid[i+1][j] == 0:
                        perimeter += 1
                    if grid[i][j+1] == 0:
                        perimeter += 1
                    if grid[i-1][j] == 0:
                        perimeter += 1
                    if grid[i][j-1] == 0:
                        perimeter += 1
        return perimeter