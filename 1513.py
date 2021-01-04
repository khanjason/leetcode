class Solution:
    def allones(self,st):
        for c in st:
            if c!='1':
                return False
        return True
    
    def cumsum(self,n):
        c=0
        for i in range(1,n+1):
            c=c+i
        return c
    
    def numSub(self, s: str) -> int:
        li=s.split('0')
        #1, 3, 6 , 9, 11111 
        #plus len of previous
        #plus factorial
        #n=1 1
        #n=2 2+previous
        #n=3 3+2+1
        #n=4 4+3+2+1
        #n=5 5+4+3+2+1
        #n=6 6+5+4+3+2+1
        count=0
        for t in li:
            if t!='':
                
                if len(t)==1:
                    count=count+1
                else:
                    count=count+(self.cumsum(len(t)))
                
        return count%(10**9 + 7)
