class Solution:
    
    def getdec(self,b):
        l=len(b)-1
        tot=0
        c=0
        for i in range(l,-1,-1):
            
            if b[c]=='1':
                tot=tot+(2**i)
            c=c+1
        return(tot)
    
    def getbin(self,n):
        s=''
        if n==0:
            return '0'
        while n>1:
            if n%2==0:
                s=s+'0'
                n=int(n/2)
            if n%2==1:
                s=s+'1'
                n=int(n/2)
        return s[::-1]
    def getcomp(self,s):
        t=''

        for thing in s:
            if thing=='0':
                t=t+'1'
            if thing=='1':
                t=t+'0'
        return(t)
        
    def bitwiseComplement(self, N: int) -> int:
        s=((self.getbin(N)))
        comp=(self.getcomp(s))
        ans=(self.getdec(comp))
        return ans
