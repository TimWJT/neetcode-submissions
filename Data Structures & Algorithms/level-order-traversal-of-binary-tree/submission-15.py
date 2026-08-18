# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if not root:
            return []

        q = deque([root])
        result = []
        
        while q:
            level_size = len(q)
            current_level = []

            for i in range(level_size):
                

                curr = q.popleft()
                current_level.append(curr)

            for n in current_level:
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)


                result.append(n.val)
        
        return result

