# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0

        def search(node, low, high):
            

            if not node:
                return

            left = search(node.left, low, high)
            right = search(node.right, low, high)
            if node.val <= high and node.val >= low:
                self.sum += node.val

            return
        
        search(root, low, high)
        return self.sum