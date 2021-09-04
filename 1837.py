class Solution:
    def tobin(self,n):
        s=''
        while n>=1:
            if n%2==0:
                s=s+'0'
            else:
                s=s+'1'
            n=int(n//2)
        return s[::-1]
    
    def sumBase(self, n: int, k: int) -> int:
        tot=''
        while n>=1:
            if n%k==0:
                tot=tot+'0'
            else:
                tot=tot+str(n%k)
            n=int(n//k)
        ans=0
        for i in tot:
            ans=ans+int(i)
        return ans