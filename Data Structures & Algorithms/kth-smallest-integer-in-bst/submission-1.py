class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.ans = None
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            
            self.count += 1
            if self.count == k:
                self.ans = node.val
                return
            
            traverse(node.right)
        
        traverse(root)
        return self.ans