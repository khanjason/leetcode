class Solution:
    def flip(self,grid):
        rlist=[]
        for row in grid:
            r=row[::-1]
            rlist.append(r)
        return rlist
    def invert(self,grid):
        for item in grid:
            for i in range(0,len(item)):
                if item[i]==1:
                    item[i]=0
                else:
                    item[i]=1
        return grid
    
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        #mirror
        #1=0
        #return
        return(self.invert(self.flip(A)))
