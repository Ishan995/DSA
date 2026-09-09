# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q=deque([root])
        ans=[]

        while q:
            lvlsize=len(q)
            tmp=[0]*lvlsize
            first=0
            last=lvlsize-1

            for i in range(lvlsize):
                t=q.popleft()
                tmp[first]=t.val
                first+=1
                
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

            ans.append(tmp)
        return ans
    






        
       

        