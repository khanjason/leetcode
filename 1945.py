class Solution:
    def transform(self,n):
        t=str(n)
        
        tot=0
        for item in t:
            tot=tot+int(item)
            
        return tot
    
    def getLucky(self, s: str, k: int) -> int:
        alp='abcdefghijklmnopqrstuvwxyz'
        st=''
        for i in s:
            st=st+str(alp.index(i)+1)
        st=int(st)
        for y in range(0,k):
            st=self.transform(st)
        return st