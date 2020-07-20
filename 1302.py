# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def GivenLevel(self,root , level,vals): 
        
        if root is None: 
            return vals
        if level == 1: 
           
            vals.append(root.val)
        elif level > 1 : 
            self.GivenLevel(root.left , level-1,vals) 
            self.GivenLevel(root.right , level-1,vals) 
        return vals
    def height(self,node): 
        if node is None: 
            return 0 
        else :  
            lheight = self.height(node.left) 
            rheight = self.height(node.right) 

            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1
    def deepestLeavesSum(self, root: TreeNode) -> int:
        h=self.height(root)
        return sum(self.GivenLevel(root,h,[]))
