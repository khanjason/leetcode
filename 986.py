class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans=[]
        p1=0
        p2=0
        while p1<len(A) and p2<len(B):
            lo=max(A[p1][0],B[p2][0])
            hi=min(A[p1][1],B[p2][1])
            if lo<= hi:
                ans.append([lo, hi])

            if A[p1][1]<B[p2][1]:
                p1=p1+1
            else:
                p2=p2+1
        return ans
            
