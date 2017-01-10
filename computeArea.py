class Solution(object):

    # O(1) time complexity. Constant space complexity.
    # Two cases when considering overlapping rectangles. 
    # Case 1: The rectangles don't overlap. Overlap == 0
    # Case 2: The rectangels do overlap. Solve for overlap.
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        return (C-A)*(D-B) + (G-E)*(H-F) - overlap
        