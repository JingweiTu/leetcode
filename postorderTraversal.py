# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # Recursive solution. O(n). Linear space complexity. 
    # Using an inner function, our base case if when we hit a None. 
    # Otherwise, we recurse through the left and then the right subtrees.
    # Finally, we append the val of the node only after we are through those subtrees.
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = []
        def recurse(node):
            if not node:
                return
            recurse(node.left)
            recurse(node.right)
            data.append(node.val)
        recurse(root)
        return data
        
        # TODO: Implement iterative solution.