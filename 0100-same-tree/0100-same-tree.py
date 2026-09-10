# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 

        def fun(root1,root2):

            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False
            
            rec1=fun(root1.left,root2.left)
            rec2=fun(root1.right,root2.right)

            if rec1==True and rec2==True:
                return True
            return False
        
        return fun(p,q)


            

            

            
    