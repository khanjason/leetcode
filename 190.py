class Solution:
    def tobin(self,n):
        s=''
        while n>0:
            if n%2==0:
                s=s+'0'
            else:
                s=s+'1'
            n=int(n/2)
        while len(s)<32:
            s=s+'0'
        return s
    
    def todec(self,s):
        tot=0
        l=len(s)-1
        n=l
        for i in s:
            if i=='1':
                tot=tot+(2**n)
            n=n-1
        return tot
    
    def reverseBits(self, n: int) -> int:
        
        r=self.tobin(n)
        #print(r)
        return self.todec(r)
