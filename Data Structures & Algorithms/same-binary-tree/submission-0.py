# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        
        # DFS: pre-order
        # NODE -> LEFT -> RIGHT

        if p.val != q.val:
            return False
        
        resLeft = self.isSameTree(p.left, q.left)
        if not resLeft:
            return False

        resRight = self.isSameTree(p.right, q.right)
        if not resRight:
            return False

        return True
        