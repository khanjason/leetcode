class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(A[0])):
            col=[]
            for c in range(len(A)):
                col.append(A[c][i])
            ans.append(col)
        return ans
                
