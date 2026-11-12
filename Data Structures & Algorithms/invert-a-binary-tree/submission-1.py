# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        from collections import deque
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr.right and curr.left:
                temp = curr.right
                curr.right = curr.left
                curr.left = temp
            elif curr.right and not curr.left:
                curr.left = curr.right
                curr.right = None
            elif not curr.right and curr.left:
                curr.right = curr.left
                curr.left = None

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        return root

        