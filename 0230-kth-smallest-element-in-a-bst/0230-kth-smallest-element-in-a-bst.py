# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        asc=[]

        def getsmall():
            if not asc:
                return None
            small=asc.pop()
            rightchild=small.right
            while rightchild:
                asc.append(rightchild)
                rightchild=rightchild.left
            return small
        
        t=root
        while t:
            asc.append(t)
            t=t.left

        curr=None
        for i in range(k):
            curr=getsmall()
        if curr:
            return curr.val
        else:
            return None


        