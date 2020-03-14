class Solution:
    def shift(self,strin):
        s=strin[0]
        strin=strin[1:]
        strin=strin+s
        return strin
    
    def rotateString(self, A: str, B: str) -> bool:
        if A==B:
                return True
        l=len(A)
        if l!=len(B):
            return False
        
        for i in range(0,l):
            if A==B:
                return True
            A=self.shift(A)
            
        return False
