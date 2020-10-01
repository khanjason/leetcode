class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        newmat = [[0 for i in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        for i in range(1,len(mat)+1):
            for j in range(1,len(mat[0])+1):
                newmat[i][j]=mat[i-1][j-1]+newmat[i-1][j]+newmat[i][j-1]-newmat[i-1][j-1] 
        for i in range(1,len(mat)+1):
            for j in range(1,len(mat[0])+1):
                r1=max(i-K-1,0)
                c1=max(j-K-1,0)
                r2=min(i+K,len(mat))
                c2=min(j+K,len(mat[0]))
                mat[i-1][j-1] =newmat[r2][c2]-newmat[r1][c2]-newmat[r2][c1]+newmat[r1][c1]
        return mat
