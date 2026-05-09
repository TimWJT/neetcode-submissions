class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            self.diameter = max(self.diameter, left + right)  # path through me
            
            return 1 + max(left, right)  # my height (for parent to use)
        
        height(root)
        return self.diameter