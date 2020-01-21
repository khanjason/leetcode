# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.unil=[]
    def depp(self,root,c):
        if root:
            c=c+1
            if root.left:
                self.unil.append(self.depp(root.left,c))
            if root.right:
                self.unil.append(self.depp(root.right,c))
        self.unil.append(c)
        return c
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            print(self.depp(root.left,1))
            print(self.depp(root.right,1))
        else:
            return 0
        return(max(self.unil))
       
