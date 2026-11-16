# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 01. approach: do a DFS post-order and add each node's value to an array
        self.post_order_traversal = []
        def dfs(root):
            # base case
            if not root:
                return 

            dfs(root.left)
            self.post_order_traversal.append(root.val)
            dfs(root.right)

        dfs(root)
        print(self.post_order_traversal)
        
        left = 0
        for right in range(1, len(self.post_order_traversal)):
            if self.post_order_traversal[left] >= self.post_order_traversal[right]:
                return False
            left += 1
        
        return True


        


