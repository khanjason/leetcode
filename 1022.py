# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def bintode(self, bi):
        tot=0
        for i in range(0,len(bi)):
            if bi[i] =='1':
               
                tot=tot+(2**((len(bi)-1)-i))
        return tot
    
    def getPaths(self, root):
        if root is None: 
            return []
        if (root.left==None and root.right==None):
            return [str(root.val)]
        return [str(root.val)+l for l in 
             self.getPaths(root.right)+self.getPaths(root.left)]

    
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        li=(self.getPaths(root))
        to=0
        for t in li:
            to=to+(self.bintode(t))
        return to
