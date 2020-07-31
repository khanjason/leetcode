class Solution:
    def Turn(self,N,i):
         if N%i==0:
            N=N-i
        
            return N
         else:
            return False
    
    def divisorGame(self, N: int) -> bool:
        isAliceTurn=True
        for i in range(1,N):
            isAliceTurn=True

            res=self.Turn(N,1)
            if res==False:
                    return False
            else:
                N=res
            isAliceTurn=False
            r=self.Turn(N,1)
            if r==False:
                return True
            else:
                N=r
