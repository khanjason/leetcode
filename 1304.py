class Solution:
    def sumZero(self, n: int) -> List[int]:
        a=[]
       
        for i in range(1,int(n/2)+1):
                a.append(i)
                a.append(-(i))
        if n % 2==1:
                a.append(0)
            
        return(a)
