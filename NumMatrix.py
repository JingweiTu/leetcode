

# Naive solution. 
class NumMatrix(object):
    
    matrix = None
    
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix    

    # O(1) time complexity. Linear space complexity. 
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.matrix[row][col] = val

    # O(n^2) time complexity. Linear space complexity. 
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                sum += self.matrix[r][c] 
        return sum

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)