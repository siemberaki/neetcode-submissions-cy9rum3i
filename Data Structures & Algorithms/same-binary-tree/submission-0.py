# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

         # Case 1: both empty
        if not p and not q:
            return True
        
        # Case 2: one empty
        if not p or not q:
            return False
        
        # Case 3: values different
        if p.val != q.val:
            return False
        
        # Case 4: check left and right
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))



        
        
      