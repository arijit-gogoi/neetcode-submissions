# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def check_balance(node: Optional[TreeNode]) -> int:
            nonlocal balanced
            if node is None:
                return 0

            left = check_balance(node.left)
            if not balanced:
                return 0
                
            right = check_balance(node.right)
            if abs(left - right) > 1:
                balanced = False
            return 1 + max(left, right)
        
        check_balance(root)
        return balanced