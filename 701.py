# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,root,node): 
        
        if root is None or ( root.val is None): 
            print('i')
            root = node 
            
        else: 
            if root.val < node.val: 
                if root.right is None: 
                    root.right = node 
                else: 
                    self.insert(root.right, node) 
            else: 
                if root.left is None: 
                    root.left = node 
                else: 
                    self.insert(root.left, node) 
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        r=root
        n=TreeNode(val=val)
        if root is None:
            root=n
            return root
        self.insert(root,n)
        return root
