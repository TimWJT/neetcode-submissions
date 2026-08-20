"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Notebook: maps original Node -> cloned Node
        visited = {}

        def dfs(current):
            # 1. If we already cloned this node, reuse it!
            if current in visited:
                return visited[current]

            # 2. Create the new copy
            clone = Node(current.val)
            visited[current] = clone  # Save it immediately

            # 3. Connect the copy's neighbors
            for neighbor in current.neighbors:
                # Recursively get the cloned neighbor and add it
                clone.neighbors.append(dfs(neighbor))

            return clone

        # Start from the root node
        return dfs(node)