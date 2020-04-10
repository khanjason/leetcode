class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s=sorted(A)
        n=int(len(A)/2)
        for i in range(0,len(A)):
            if(A.count(A[i]))==n:
                return A[i]
