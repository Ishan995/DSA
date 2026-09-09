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
        q = deque([root])
        ans = []
        
        while q:
            lvlSize = len(q)       # int lvlsize = q.size();
            tmp = []               # vector<int> tmp;
            
            while lvlSize > 0:     # while (lvlSize--)
                t = q.popleft()    # Node* t = q.front(); q.pop();
                tmp.append(t.val)  # tmp.push_back(t->data);
                
                if t.left:         # if (t->left != null)
                    q.append(t.left) # q.push(t->left);
                    
                if t.right:        # if (t->right != null)
                    q.append(t.right) # q.push(t->right);
                
                lvlSize -= 1       # Manual decrement (the '--' part)
            
            ans.append(tmp)        # res.push_back(tmp);
            
        return ans






        
       

        