class Solution:
    def coordston(self,x,y,m,n):
        return (x*n)+(y)
        
    def ntocoord(self,t,m,n):
        
        while t>((m*n)-1):
            t=t-((m*n))
        
        x=int(t/n)
        y=t%n
        
        return([x,y])
    
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #take in coords and convert to list n
        #take list n and convert to coords
        
        m=len(grid)
        n=len(grid[0])
        if n==1 and m==1:
            return grid
        
        ans=[]
        
        for row in grid:
            
            a=[]
            for i in row:
                
                a.append(0)
                
            ans.append(a)
        for x in range(0,m):
            for y in range(0,n):
                tot=self.coordston(x,y,m,n)
                tot=tot+k
                coords=(self.ntocoord(tot,m,n))
                print(coords)
                coordx=coords[0]
                coordy=coords[1]
                ans[coordx][coordy]=grid[x][y]
        return ans
