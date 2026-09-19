# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = 0 #index of preorder array #start from first index because preorder is root,left,right
        inorder_map = {}

        # 1. Store inorder value -> index for O(1) lookup
        for index, val in enumerate(inorder):
            inorder_map[val] = index

        def fun(preorder, low, high):
            nonlocal idx  
            
            # Base case: valid inorder range exhausted
            if low > high:
                return None

            # 2. First element in preorder range is always current root
            node = TreeNode(preorder[idx])
            idx += 1

            # 3. Find root location in inorder array to divide subtrees
            id = inorder_map[node.val]

            # 4. Recursively build left (low to id-1) then right (id+1 to high)
            node.left = fun(preorder, low, id - 1)
            node.right = fun(preorder, id + 1, high)

            return node

        return fun(preorder, 0, len(inorder) - 1)



        