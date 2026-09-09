# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        ans = []
        leftToRight = True
        
        while q:
            lvlSize = len(q)
            # Pre-allocate array of size lvlSize
            temp = [0] * lvlSize  
            
            first = 0
            last = lvlSize - 1
            
            for i in range(lvlSize):
                t = q.popleft()
                
                # Fill array from front (left-to-right) or back (right-to-left)
                if leftToRight:
                    temp[first] = t.val
                    first += 1      # first++
                else:
                    temp[last] = t.val
                    last -= 1       # last--
                
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            
            ans.append(temp)
            leftToRight = not leftToRight  # Flip direction for next level
            
        return ans




        