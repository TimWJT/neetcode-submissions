# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return
        


        return max(maxDepth(root.left) + 1, maxDepth(root.right) + 1)



        # def traverse(node):

            
        #     traverse(node.left)
        #     traverse(node.right)
        

        # traverse(root)
        # return max_depth