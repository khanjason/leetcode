# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,d):
        
        if root: 

            d.append(root.val), 
            self.preorder(root.left,d) 
            self.preorder(root.right,d) 
        return d
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        d=self.preorder(root,[])
        d=sorted(d)
        return d[k-1]
