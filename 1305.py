# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printInorder(self,root,res): 
  
        if root: 

            self.printInorder(root.left,res) 

            res.append(root.val) 

            self.printInorder(root.right,res) 
        return res
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res=[]
        res=self.printInorder(root1,res)
        res=self.printInorder(root2,res)
        return sorted(res)
