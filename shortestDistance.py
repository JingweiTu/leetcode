class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return -1
        M = len(grid)
        N = len(grid[0])
        buildings = sum(val for line in grid for val in line if val == 1)
        hit = [[0] * N for i in range(M)]
        distSum = [[0] * N for i in range(M)]
        
        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y] = True 
            count1 = 1 
            # a double ended queue containing the coordinates and distance away from x,y that
            # particular coordinate is.
            queue = collections.deque([(start_x, start_y, 0)])
            
            while queue:
                x, y, dist = queue.popleft()
                directions = set([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

                # For each pair of directions to search, we check to see that they are valid
                # and that they have not been visited before. 
                for i, j in directions:
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        # mark that coordinate True in the local visited matrix.
                        visited[i][j] = True
                        # If the coordinate's value is zero (ie, it is passable), we add it
                        # to the queue, so we can explore it further. 
                        if grid[i][j] == 0:
                            queue.append((i, j, dist + 1))
                            # Since we only run BFS whenever we find a 1 (outside of this 
                            # BFS function), hit is a matrix that indicates that this 
                            # particular index was reached by the 1 from which we started 
                            # the BFS. Ideally, after we cycle through all the 1s, 
                            # if hit[i][j] == # of 1s, it means all buildings can be reached
                            # from i,j.
                            hit[i][j] += 1
                            # increment the sum of the distances from every building visited
                            # thus far to i,j.
                            distSum[i][j] += dist + 1
                        # if we reach a building, we just increment count1. We can search no
                        # further.
                        elif grid[i][j] == 1:
                            count1 += 1
                        # The only other case, we hit a 2, we do nothing.
                        else:
                            continue
            # return whether or not we can reach all the buildings.
            return count1 == buildings  
        
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y): 
                        return -1
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])
