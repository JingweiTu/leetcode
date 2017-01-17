# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # We've passed a leaf node, so return 0.
        if root == None:
            return 0
        
        # If either left or right is None, we don't really care, because minDepth(None) == 0. 
        # We add 1 for the current node and we continue the DFS on the left and right nodes.
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        
        # If both sides are not empty, we want the min of their depth. Add 1 for the current
        # node.
        return min(self.minDepth(root.right),self.minDepth(root.left))+1
        
        