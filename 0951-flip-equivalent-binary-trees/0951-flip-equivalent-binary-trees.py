# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:

        def fun(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            
            no_flip=fun(p.left, q.left) and fun(p.right, q.right)
            flip=fun(p.left, q.right) and fun(p.right, q.left)

            return no_flip or flip
        
        return fun(root1,root2)




        