# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        # []
        res = []
        # [[1], [2, 3], [4, 5]]
        while q:
            level_size = len(q)
            # 2
            current_level = []
            for _ in range(level_size): # 2
                curr_node = q.popleft() # 5
                current_level.append(curr_node.val)
                # [4, 5]
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res.append(current_level)

        return res

