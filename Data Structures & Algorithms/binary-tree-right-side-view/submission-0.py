# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS

        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            res.append(q[-1].val)
            level_size = len(q) # 1 -> [5]

            for _ in range(level_size): # 1
                curr_node = q.popleft()

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            


        return res 


