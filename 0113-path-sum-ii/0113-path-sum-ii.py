# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        diary=[]

        def fun(root,sum):
            nonlocal res,diary
            if not root:
                return 
            sum=sum+root.val
            diary.append(root.val)

            if not root.left and not root.right:
                if sum==targetSum:
                    res.append(diary.copy())
                diary.pop()
                return

            if root.left:
                fun(root.left,sum)
            if root.right:
                fun(root.right,sum)
            diary.pop()
            return

        fun(root,0)
        return res


        