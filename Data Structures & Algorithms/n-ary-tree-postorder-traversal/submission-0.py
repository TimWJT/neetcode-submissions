"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        


        output = []

        def traverse(node):

            if not node:
                return

            for c in node.children:
                traverse(c)
            output.append(node.val)

        traverse(root)
        return output