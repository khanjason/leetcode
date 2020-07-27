# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def LevelOrder(self,root,li): 
        h = self.height(root) 
        for i in range(1, h+1): 
            k=self.GivenLevel(root, i,[]) 
            avg=(sum(k)/len(k))
            li.append(avg)
        return li
 
    def GivenLevel(self,root , level,arr): 
        if root is None: 
            return arr
        if level == 1: 
            arr.append(root.val) 
        elif level > 1 : 
            self.GivenLevel(root.left , level-1,arr) 
            self.GivenLevel(root.right , level-1,arr) 
        return arr

    def height(self,node): 
        if node is None: 
            return 0 
        else : 
      
            lheight = self.height(node.left) 
            rheight = self.height(node.right) 

 
            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1
    
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        return self.LevelOrder(root,[])
