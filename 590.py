"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def Postorder(self,root): 
        res=[]
        if root: 

            for i in root.children:
                res=res+self.Postorder(i) 

          
            # now print the data of node 
            res.append(root.val)
        return res
  
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.Postorder(root)
