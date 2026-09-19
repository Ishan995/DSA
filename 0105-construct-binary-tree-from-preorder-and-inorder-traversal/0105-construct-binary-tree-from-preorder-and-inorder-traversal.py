# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        idx=0
        #hasmap for lookup in inorder array
        in_map={}
        for index,val in enumerate(inorder):
            in_map[val]=index
        def fun(preorder,low,high):
            nonlocal idx
            if low>high:
                return None
            node=TreeNode(preorder[idx])
            idx+=1
            id=in_map[node.val]
            node.left=fun(preorder,low,id-1)
            node.right=fun(preorder,id+1,high)
            return node
        return fun(preorder,0,len(inorder)-1)





        