# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
       # DIFFERENCE FROM LC 105: Start at end because Postorder structure is [Left, Right, Root]
        idx = len(postorder) - 1
        inorder_map = {}

        # 1. Store inorder value -> index for O(1) lookup (SAME AS LC 105)
        for index, val in enumerate(inorder):
            inorder_map[val] = index

        def fun(postorder, low, high):
            nonlocal idx  # Track pointer across recursive calls (SAME AS LC 105)
            
            # Base case: valid inorder range exhausted (SAME AS LC 105)
            if low > high:
                return None

            # 2. Root is current postorder element; decrement pointer (LC 105 used idx += 1)
            node = TreeNode(postorder[idx])
            idx -= 1

            # 3. Find root location in inorder array to divide subtrees (SAME AS LC 105)
            id = inorder_map[node.val]

            # 4. CRITICAL DIFFERENCE FROM LC 105: Build RIGHT subtree first, then LEFT!
            # Since postorder is [Left, Right, Root], going backwards gives [Root, Right, Left].
            node.right = fun(postorder, id + 1, high)
            node.left = fun(postorder, low, id - 1)

            return node

        return fun(postorder, 0, len(inorder) - 1)
            

        