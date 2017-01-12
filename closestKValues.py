# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution(object):

    # O(nlogn) time complexity. Linear space complexity.
    # Recursively visit all the nodes in the tree and add them to node_heap (which is a min
    # heap) in the form (abs(target - root.val),root.val)), so the nodes will be sorted by
    # their distance from the target (abs(target - root.val))
    # Pop the first k values of node_heap and return them.
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        node_heap = []
        def recurse(node_heap,root):
            if root:
                heapq.heappush(node_heap,(abs(target - root.val),root.val))
                recurse(node_heap,root.left)
                recurse(node_heap,root.right)
                
        recurse(node_heap,root)
        output = []
        for i in range(k):
            output.append(heapq.heappop(node_heap)[1])
        return output
