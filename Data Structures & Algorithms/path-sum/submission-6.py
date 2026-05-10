# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        if not root:
            return False
        
        newTargetSum = targetSum - root.val
        
        if not root.left and not root.right and newTargetSum == 0:
            return True
        
        left = self.hasPathSum(root.left, newTargetSum)
        if left == True:
            return True
        right = self.hasPathSum(root.right, newTargetSum)
        if right == True:
            return True

        return False