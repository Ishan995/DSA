# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return None

        asc=[]
        desc=[]

        def getsmall():
            if not asc:
                return None
            small=asc.pop()
            rightchild=small.right
            while rightchild:
                asc.append(rightchild)
                rightchild=rightchild.left
            return small
        
        def getbig():
            if not desc:
                return None
            big=desc.pop()
            leftchild=big.left
            while leftchild:
                desc.append(leftchild)
                leftchild=leftchild.right
            return big 
        
        t=root
        while t:
            asc.append(t)
            t=t.left

        t=root
        while t:
            desc.append(t)
            t=t.right

        i=getsmall()
        j=getbig()

        while i and j and i!=j and i.val<j.val:
            curr_sum=i.val+j.val
            if curr_sum==k:
                return True
            if curr_sum<k:
                i=getsmall()
            else:
                j=getbig()
        return False



        

    
        

          
        