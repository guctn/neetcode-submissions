# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr_node = root 
        right = max(q.val, p.val)
        left = min(q.val, p.val)

        while curr_node:
            if curr_node.val >= left and curr_node.val <= right:
                return curr_node
            elif left < curr_node.val and right < curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
