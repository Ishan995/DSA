# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None  # Node* ans;

        def fun(node, p, q):
            nonlocal ans
            
            # if (node == null)
            if not node:
                return 0
            
            # int left = fun(node->left, p, q);
            left = fun(node.left, p, q)
            
            # int right = fun(node->right, p, q);
            right = fun(node.right, p, q)
            
            # int self = 0;
            self_val = 0
            
            # if (node == p or node == q) self = 1;
            if node == p or node == q:
                self_val = 1
                
            # int total = left + self + right;
            total = left + self_val + right
            
            # if (total == 2 and ans == null) ans = node;
            if total == 2 and ans is None:
                ans = node
                
            # return total;
            return total

        fun(root, p, q)
        return ans
                

        
        