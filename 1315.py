# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getgrandkid(self,n):
        grandkids=[] #vals
        if n.left:
            t=n.left
            if t.left:
                grandkids.append(t.left.val)
            if t.right:
                grandkids.append(t.right.val)
        if n.right:
            t=n.right
            if t.left:
                grandkids.append(t.left.val)
            if t.right:
                grandkids.append(t.right.val)
        return grandkids
          
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            if root.val %2==0:
                res.append(self.getgrandkid(root))
            res = res + self.inorderTraversal(root.right)
        return res
        
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        tot=0
        lioli=(self.inorderTraversal(root))
        for li in lioli:
            tot=tot+sum(li)
        return tot
