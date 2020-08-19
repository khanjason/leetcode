# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder(self,n,s):
        if not n: 
            return s

        n.val += self.postorder(n.right, s)
        return self.postorder(n.left, n.val)
    
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
    
        self.postorder(root, 0)
        return root
