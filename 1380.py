class Solution:
    
    def getcolumns(self,item,matrix):
        li=[]
        for i in matrix:
            li.append(i[item])
        return li
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        colmax=False
        rowlow=False
        lucks=[]
        for row in matrix:
            for item in range(0,len(row)):
                colmax=False
                rowlow=False
                if min(row)==row[item]:
                    rowlow=True
                if max(self.getcolumns(item,matrix))==row[item]:
                    colmax=True
                if (rowlow and colmax):
                    lucks.append(row[item])
        return(lucks)
                
                
