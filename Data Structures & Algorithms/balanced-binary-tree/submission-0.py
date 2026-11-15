# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root) -> int:
            # base-case
            if not root:
                return 0

            depth_left = dfs(root.left)
            depth_right = dfs(root.right)
            if (depth_left or depth_right) == -1:
                return -1
            elif abs(depth_left - depth_right) > 1:
                return -1
            else:
                return 1 + max(depth_left, depth_right)
        
        return True if dfs(root) >= 0 else False
            