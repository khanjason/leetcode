class Solution:
    def converttobin(self,n):
        s=''
        while n>=1:
            if n%2==0:
                s=s+'0'
            else:
                s=s+'1'
            n=int(n/2)
        return s[::-1]
                
    def padded(self,x,y):
        m=max(len(x),len(y))
        size=m+1
        a=''
        b=''
        for t in range(0,size-len(x)):
            a=a+'0'
        size2=len(y)
        for p in range(0,size-len(y)):
            b=b+'0'
        ans1=a+x
        ans2=b+y
        return (ans1,ans2)
    def hammingDistance(self, x: int, y: int) -> int:
        binx=self.converttobin(x)
        biny=self.converttobin(y)
        pads=self.padded(binx,biny)
        padx=pads[0]
        pady=pads[1]
        
        count=0
        start=False
        for i in range(len(padx)):
            
            if padx[i]!=pady[i]:
                count+=1
                
        return(count)
                
