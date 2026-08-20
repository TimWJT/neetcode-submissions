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
        visited = {}

        def dfs(current):
            if not current:
                return None
            
            if current in visited:
                return visited[current]
            
            new_node = Node(current.val)
            visited[current] = new_node

            for neighbor in current.neighbors:
                
                new_node.neighbors.append(dfs(neighbor))
                
            return new_node

        return dfs(node)








