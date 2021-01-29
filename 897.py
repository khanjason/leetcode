# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # A function to do inorder tree traversal 
    def printInorder(self,root,li): 

        if root: 

            self.printInorder(root.left,li) 

            li.append(root.val)

            self.printInorder(root.right,li) 
        return li

    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals=self.printInorder(root,[])
        
        prev=TreeNode()
        root=prev
        for i in range(0,len(vals)):
            if i==0:
                prev.val=vals[i]
            else:
                n=TreeNode(val=vals[i])
                prev.right=n
                prev=n
        return root
