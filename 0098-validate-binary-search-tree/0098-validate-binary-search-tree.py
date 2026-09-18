# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev=None
        ans=True
        def fun(root):
            nonlocal prev,ans
            if root is None:
                return 
            
            fun(root.left)

            if prev is None:
                prev=root
            else:
                if root.val<=prev.val:
                    ans=False
                prev=root
            
            fun(root.right)


        fun(root)
        return ans

        