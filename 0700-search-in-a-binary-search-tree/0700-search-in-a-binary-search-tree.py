# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans=None
        def fun (node,k):
            nonlocal ans
            
            if not node:
                return None
            
            if node.val==k:
                ans=node
                return ans 
            if node.val>k:
                fun(node.left,k)
            else:
                fun(node.right,k)
            
            return ans

        fun(root,val)
        return ans

            