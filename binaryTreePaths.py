# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    # O(n) time complexity. Linear space complexity.
    # Keep pushing the latest node to the stack and popping it until we reach a leaf node. 
    # At each iteration, if a left or right node exist for the current node. If so, 
    # append str(node.val)+"->" to the current string and push the respective right and/or 
    # left node, along with the new string, to the stack. Otherwise, if we reach a leaf
    # node, just append its value to string and append string to output.
    def binaryTreePaths(self, root):
        if not root:
            return []
        output, stack = [], [(root, "")]
        while stack:
            node, string = stack.pop()
            if not node.left and not node.right:
                output.append(string+str(node.val))
            if node.right:
                stack.append((node.right, string+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, string+str(node.val)+"->"))
        return output