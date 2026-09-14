# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res=False
        def fun(root,sum):
            nonlocal res

            # root==null
            if not root:
                return 
            sum=sum+root.val

            #if leaf node
            if not root.left and not root.right:
                if sum==targetSum:
                    res=True 
                return False

            #non leaf node
            if root.left:
                fun(root.left,sum)
            if root.right:
                fun(root.right,sum)
                
                
        fun(root,0)
        return res
            
            
            



        