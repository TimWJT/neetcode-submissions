# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        


        # if current node is same as subroot, use isSameTree to check
        # if current node isnt the same, then recurse to child node

        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, q, p):
        
        if q is None and p is None:
            return True
        if q is None or p is None:
            return False

        
        if q.val != p.val:
            return False

        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

