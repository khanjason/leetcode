# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Postorder(self,root,target,li): 
  
        if root: 

            self.Postorder(root.left,target,li) 

            self.Postorder(root.right,target,li) 

            v=(root.val)
            if v==target:
                li.append(root)
        return li
        
  
    
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        targetval=target.val
        return (self.Postorder(cloned,targetval,[]))[0]
