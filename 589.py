"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preordertrav(self,root,li): 
  
        if root: 

           
            li.append(root.val)
            for i in root.children:
                self.preordertrav(i,li)
        return li
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        li=[]
        return self.preordertrav(root,li)
