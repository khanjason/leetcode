# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,r):
        
        if r:
            if not r.left:
                return self.inorder(r.right)+1
            if not r.right:
                return self.inorder(r.left)+1
            return min(self.inorder(r.left), self.inorder(r.right))+1
        return 0
       

    def minDepth(self, root: TreeNode) -> int:
        
        l=(self.inorder(root))
        return l
