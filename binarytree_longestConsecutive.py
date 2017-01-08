# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans, dq = 0, deque([[root, 1]])
        while dq:
            node, length = dq.popleft()
            ans = max(ans, length)
            for child in [node.left, node.right]:
                if child:
                    l = length + 1 if child.val == node.val + 1 else 1
                    dq.append([child, l])
        return ans
        