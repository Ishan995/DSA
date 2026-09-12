# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        def fun(root,p,q):
            #assume p.val<q.val
            nonlocal ans 
            if not root:
                return ans 
            if root.val==p.val or root.val==q.val:
                ans=root
                return ans
            elif root.val>q.val>p.val: 
                fun(root.left,p,q)
            elif root.val<p.val<q.val: 
                fun(root.right,p,q)
            elif (root.val>p.val and root.val<q.val):
                ans=root
                return ans
            
        if p.val<q.val:
            fun(root,p,q)
        else:
            fun(root,q,p)
        return ans

