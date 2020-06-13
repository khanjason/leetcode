class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
        return

class Solution:
    def getAns(self,n,root):
            pN = p1 = root
            ans = 0
            i = 1 << 30
            while i:
                if n & i:
                    if not pN.right:
                        pN.right = TrieNode()
                    pN = pN.right
                    if p1.left:
                        p1=p1.left
                        ans=ans+i
                    else:
                        p1=p1.right
                else:
                    if not pN.left:
                        pN.left=TrieNode()
                    pN=pN.left
                    if p1.right:
                        p1=p1.right
                        ans=ans+i
                    else:
                        p1=p1.left
                i >>= 1
            return ans
    
    
    
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        root=TrieNode()
        ans=0
        for n in nums:
            ans=max(ans, self.getAns(n,root))
        return ans

