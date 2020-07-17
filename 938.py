# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        tot=[]
        return sum(self.Inorder(root,L,R,tot))
        
    def Inorder(self,root,L,R,tot): 
        
        if root: 

            self.Inorder(root.left,L,R,tot) 

            if (root.val)>=L and R>=(root.val):
                
                tot.append(root.val)

            # now recur on right child 
            self.Inorder(root.right,L,R,tot) 
        
        return tot
