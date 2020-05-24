from collections import defaultdict
class Solution:
    def getpow(self,n):
        c=0
        while n!=1:
            c=c+1
            if n%2==0:
                
                n=n/2
                #print(n)
            else:
                
                n=(n*3)+1
                #print(n)
        return c
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        li=[]
        ans=[]
        d = defaultdict(int)
        for i in range(lo,hi+1):
            li.append(self.getpow(i))
            d[i]=(self.getpow(i))
        for w in sorted(d, key=d.get, reverse=False):
            
            ans.append(w)
        print(ans)
        return ans[k-1]
