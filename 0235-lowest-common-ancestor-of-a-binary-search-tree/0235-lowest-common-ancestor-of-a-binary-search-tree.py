# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def fun(root, p, q):
            # Assumes p.val < q.val
            nonlocal ans 
            
            if not root:
                return 
            
            if root.val == p.val or root.val == q.val:
                ans = root
                return 
            
            # If current root is larger than the bigger target (q), 
            # both p and q must be in the left subtree.
            elif root.val > q.val: 
                fun(root.left, p, q)
            
            # If current root is smaller than the smaller target (p), 
            # both p and q must be in the right subtree.
            elif root.val < p.val: 
                fun(root.right, p, q)
            
            # Current root is strictly between p and q (p.val < root.val < q.val).
            # The paths split here, so this node is the Lowest Common Ancestor.
            else:
                ans = root
                return 

        if p.val < q.val:
            fun(root, p, q)
        else:
            fun(root, q, p)
            
        return ans
