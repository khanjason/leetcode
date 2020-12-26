class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        #coords set
        s=set()
        for i in range(0,len(mat)):
            s.add((i,i))
            s.add((i,len(mat)-(i+1)))
        tot=0
        for coords in s:
            x=coords[0]
            y=coords[1]
            tot=tot+mat[x][y]
        return tot
        
