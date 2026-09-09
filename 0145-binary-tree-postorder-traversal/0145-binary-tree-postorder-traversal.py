# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans=[]
        
        def fun(node):
            if not node:
                return

            fun(node.left)
            fun(node.right)
            ans.append(node.val)
        fun(root)
        return ans