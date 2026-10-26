# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def get_max(node):
            if not node:
                return 0
            l_max = get_max(node.left)
            r_max = get_max(node.right)
            l_max = max(l_max, 0)
            r_max = max(r_max, 0)
            res[0] = max(res[0], node.val + l_max + r_max)
            return node.val + max(l_max, r_max)
        get_max(root)
        return res[0]