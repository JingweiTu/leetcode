# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Recursive solution. O(n) runtime, because it is a tree traversal. Linear space complexity.
    # Concise (although it could be more readable). Recursively search through tree, taking 
    # advantage of the fact that changing any node's root does not affect it. 
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
