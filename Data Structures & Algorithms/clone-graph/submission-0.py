"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        previous = node    
        new_head = Node(node.val)

    
        def traverse(current, new_current):

            if not current:
                return
            if not new_current:
                new_current = Node(current.val)


            for n in current.neighbours:
                new_current.neighbours.append(Node(n.val))
                traverse(n, new_current.next)


        traverse(node, new_head)
        return new_head

