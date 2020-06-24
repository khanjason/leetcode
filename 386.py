class Solution:
    def lexsort(self,n):
        s=[]
        for i in range(1,n+1):
            s.append(str(i))
        s=sorted(s)
        ans=[]
        for i in range(0,n):
            ans.append(int(s[i]))
        return ans
    
    def lexicalOrder(self, n: int) -> List[int]:
        
        return self.lexsort(n)
        
