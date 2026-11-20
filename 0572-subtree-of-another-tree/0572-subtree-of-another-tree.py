# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def same_tree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False

            rec1=same_tree(p.left,q.left)
            rec2=same_tree(p.right,q.right)

            if rec1==True and rec2==True:
                return True 
            return False
        
        def fun(curr):

            if not curr:
                return False

            if same_tree(curr,subRoot):
                return True 

            left_has=fun(curr.left)
            right_has=fun(curr.right)

            if left_has==True or right_has==True:
                return True
            return False
        
        return fun(root)
        