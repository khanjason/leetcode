class Solution:
    
    def tobin(self,n):
        s=''
        while n>=1:
            if n%2==0:
                s=s+'0'
                n=int(n/2)
            else:
                s=s+'1'
                n=int(n/2)
        return s[::-1]
    def binaryGap(self, N: int) -> int:
        b=(self.tobin(N))
        counts=[0]
        for i in range(0,len(b)):
            if b[i]=='1':
                count=0
                for t in range(i+1,len(b)):
                    count=count+1
                    if b[t]=='1':
                        counts.append(count)
                        break
        return max(counts)
