# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root,target):
        
        if root==None:
            return root
        root.left=self.inorderTraversal(root.left,target)
        root.right=self.inorderTraversal(root.right,target)
        if root.left==root.right and root.val==target:
            root=None
        return root
            
        
        return res
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        li=self.inorderTraversal(root,target)
        return li
