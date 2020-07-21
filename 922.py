class Solution:
    def even(self,L):
        for x in range(0,L,2):
            yield x
            
    def odd(self,L):
        for x in range(1,L,2):
            yield x
   
    
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        a2=[0]*len(A)
        gen=self.even(len(A))
        gen2=self.odd(len(A))
        for i in range(0,len(A)):
            if A[i]%2==0:
                ind=(next(gen))
                a2[ind]=A[i]
            else:
                ind=next(gen2)
                a2[ind]=A[i]
        return a2
        
