class Solution:
    def inc(self,mat,ind):
        r=ind[0]
        c=ind[1]
        for i in range(0,len(mat[r])):
            mat[r][i]=mat[r][i]+1
        for item in range(0,len(mat)):
            mat[item][c]=mat[item][c]+1
        
        return mat
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat=[]
        for l in range(0,n):
            tmp=[]
            for t in range(0,m):
                tmp.append(0)
            mat.append(tmp)
        for ind in indices:
            mat=self.inc(mat,ind)
        oddcount=0
        for row in mat:
            for item in row:
                if item % 2==1:
                    oddcount+=1
        return oddcount
