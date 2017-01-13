# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # O(n) time complexity. # Linear space complexity.
    # Recurse through all the nodes in the tree and add them to the serialized list,
    # If a node is None, append "#". Thus, every three elements represent 
    # root.val/root.left.val/root.right.val
    # Return the list as a string, delimited by " ".
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        def recurse(root):
            if root:
                serialized.append(str(root.val))
                recurse(root.left)
                recurse(root.right)
            else:
                serialized.append("#")
        
        recurse(root)
        return " ".join(serialized)
        

    # O(1) time complexity. Constant space complexity.
    # We have a function buildTree() that takes in an iterator vals and constructs the tree
    # recursively.
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildTree(vals):
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = buildTree()
            node.right = buildTree()
            return node

        vals = iter(data.split())
        root = buildTree(vals)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))