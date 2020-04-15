class Solution:
    
    def binone(self,n):
        c=0
        while n>=1:
            if n % 2==1:
                c=c+1
            n=int(n/2)
                
                    
        return c
    
    def countBits(self, num: int) -> List[int]:
        arr=[]
        for i in range(0,num+1):
            arr.append(self.binone(i))
        return arr
