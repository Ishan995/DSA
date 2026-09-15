# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        ans=True
        def fun(root):
            nonlocal ans
            if not root:
                return 0
            left=fun(root.left)
            right=fun(root.right)
            
            if abs(left-right)>1:
                ans=False
            return 1+max(left,right)
        fun(root)
        return ans


        