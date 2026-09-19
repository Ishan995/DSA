# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        prev=None
        g1first=None
        g1second=None
        g2first=None
        g2second=None
        galat=0

        def fun(root):
            nonlocal prev,g1first,g1second,g2first,g2second,galat
            if not root:
                return

            fun(root.left)

            if prev is None:
                prev=root
            else:
                if root.val<prev.val:
                    if galat==0:
                        g1first=prev
                        g1second=root
                        galat+=1
                    else:
                        g2first=prev
                        g2second=root
                        galat+=1
                prev=root

            fun(root.right)

        fun(root)
        if galat==1:
            g1first.val,g1second.val=g1second.val,g1first.val
        else:
            g1first.val,g2second.val=g2second.val,g1first.val



     
       
        