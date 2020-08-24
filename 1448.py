# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorder(self, root,parent):
        if not root:
            return 0
        if root.val >= parent:
            self.count = self.count+1
        left=self.inorder(root.left, max(root.val, parent))
        right=self.inorder(root.right, max(root.val, parent))
        return (left+right)
        

        
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.inorder(root, float('-inf'))
        return self.count
            
