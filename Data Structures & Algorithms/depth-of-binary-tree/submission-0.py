# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 1
        nodes_stack= [[root, 1]]

        while nodes_stack:
            node, depth = nodes_stack.pop()
            if node.right:
                nodes_stack.append([node.right, depth + 1])

            if node.left:
                nodes_stack.append([node.left, depth + 1])

            res = max(res, depth)
        return res