# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Inorder(self,root,target): 
  
        if root: 

            if self.Inorder(root.left,target) ==False:
                return False
            
            if root.val!=target:
                return False

            if self.Inorder(root.right,target) == False:
                return False
        
        return True

  
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        target=root.val
        return self.Inorder(root,target)
