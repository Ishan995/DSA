# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=0
        def fun(root,sum):
            nonlocal res

            if not root:
                return
            sum=sum*10+root.val

            if not root.left and not root.right:
                res=res+sum
        
            if root.left:
                fun(root.left,sum)
            if root.right:
                fun(root.right,sum)
        fun(root,0)
        return res
        
    

         

        