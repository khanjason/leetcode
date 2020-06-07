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
    
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1,N+1):
            if (self.tobin(i)) not in S:
                return False
        return True
