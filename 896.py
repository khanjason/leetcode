class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc=False
        dec=False
        for i in range(0,len(A)-1):
            if A[i]<A[i+1]:
                if dec==True:
                    return False
                else:
                    inc=True
            elif A[i]>A[i+1]:
                if inc==True:
                    return False
                else:
                    dec=True
        return True
