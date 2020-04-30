class Solution:
    
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #(0,0) (1,1) (2,2)
        #(1,0) (2,1)
        res=True
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if i!=(len(matrix)-1) and j!=(len(matrix[0])-1):
                    if matrix[i+1][j+1]!= matrix[i][j]:
                        return False
        return res
