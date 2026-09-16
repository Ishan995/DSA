# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        null_seen=False
        q=deque([root])

        while q:
            t=q.popleft()
            if t is None:
                null_seen=True
            else:
                if null_seen==True:
                    return False
                q.append(t.left)
                q.append(t.right)

        return True

        