# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    # O(n^2) time complexity. Linear space complexity.
    # The point is to start at the root node and search through its neighbors, adding 
    # each newly encountered node to a dictionary of visited nodes and their neighbors,
    # as well as a stack so that it can be explored later in the function. We keep 
    # popping from the stack until we have emptied it.
    def cloneGraph(self, node):
        # If empty, then return
        if not node:
            return node

        # Create new node called root.
        root = UndirectedGraphNode(node.label)
        # Stack of newly encountered nodes.
        new_nodes = [node]
        # We keep a dictionary of visited nodes to prevent infinite loops.
        visited = {}
        # Add first node to visited.
        visited[node.label] = root

        # while there are still unexplored nodes
        while stack:
            current_node = stack.pop()
        
            for n in current_node.neighbors:
                # If we encounter a new node in current_node's neighbors, we add it to the stack
                if n.label not in visited:
                    stack.append(n)
                    # We add that neighbor node to visited. 
                    visited[n.label] = UndirectedGraphNode(n.label)
                # We add the neighbor node to our visited nodes dictionary.
                visited[current_node.label].neighbors.append(visited[n.label])
        
        return root