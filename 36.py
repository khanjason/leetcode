class Solution:
    
    #get designated square from row and c number
    def getsquare(self,r,c,board):
        #relative to the r and c % 3
        
        tmp=[]
        if r%3==0 and c%3==0:
            #print(upper left)
            tmp.append(board[r][c+1])
            tmp.append(board[r][c+2])
            tmp.append(board[r+1][c])
            tmp.append(board[r+1][c+1])
            tmp.append(board[r+1][c+2])
            tmp.append(board[r+2][c])
            tmp.append(board[r+2][c+1])
            tmp.append(board[r+2][c+2])
        elif r%3==0 and c%3==1:
            #print(upper middle)
            tmp.append(board[r][c+1])
            tmp.append(board[r][c-1])
            tmp.append(board[r+1][c])
            tmp.append(board[r+1][c+1])
            tmp.append(board[r+1][c-1])
            tmp.append(board[r+2][c])
            tmp.append(board[r+2][c+1])
            tmp.append(board[r+2][c-1])
            
        elif r%3==0 and c%3==2:
            #print(upper right)
            tmp.append(board[r][c-1])
            tmp.append(board[r][c-2])
            tmp.append(board[r+1][c])
            tmp.append(board[r+1][c-1])
            tmp.append(board[r+1][c-2])
            tmp.append(board[r+2][c])
            tmp.append(board[r+2][c-1])
            tmp.append(board[r+2][c-2])
        elif r%3==1 and c%3==0:
            #print(middle left)
            tmp.append(board[r][c+1])
            tmp.append(board[r][c+2])
            tmp.append(board[r+1][c])
            tmp.append(board[r+1][c+1])
            tmp.append(board[r+1][c+2])
            tmp.append(board[r-1][c])
            tmp.append(board[r-1][c+1])
            tmp.append(board[r-1][c+2])
        elif r%3==1 and c%3==1:
            #print(middle middle)
            tmp.append(board[r][c+1])
            tmp.append(board[r][c-1])
            tmp.append(board[r+1][c])
            tmp.append(board[r+1][c+1])
            tmp.append(board[r+1][c-1])
            tmp.append(board[r-1][c])
            tmp.append(board[r-1][c+1])
            tmp.append(board[r-1][c-1])
        elif r%3==1 and c%3==2:
            #print(middle right)
            tmp.append(board[r][c-1])
            tmp.append(board[r][c-2])
            tmp.append(board[r+1][c])
            tmp.append(board[r+1][c-1])
            tmp.append(board[r+1][c-2])
            tmp.append(board[r-1][c])
            tmp.append(board[r-1][c-1])
            tmp.append(board[r-1][c-2])
        elif r%3==2 and c%3==0:
            #print(lower left)
            tmp.append(board[r][c+1])
            tmp.append(board[r][c+2])
            tmp.append(board[r-2][c])
            tmp.append(board[r-2][c+1])
            tmp.append(board[r-2][c+2])
            tmp.append(board[r-1][c])
            tmp.append(board[r-1][c+1])
            tmp.append(board[r-1][c+2])
        elif r%3==2 and c%3==1:
            #print(lower middle)
            tmp.append(board[r][c+1])
            tmp.append(board[r][c-1])
            tmp.append(board[r-2][c])
            tmp.append(board[r-2][c+1])
            tmp.append(board[r-2][c-1])
            tmp.append(board[r-1][c])
            tmp.append(board[r-1][c+1])
            tmp.append(board[r-1][c-1])
        elif r%3==2 and c%3==2:
            #print(lower right)
            tmp.append(board[r][c-1])
            tmp.append(board[r][c-2])
            tmp.append(board[r-2][c])
            tmp.append(board[r-2][c-1])
            tmp.append(board[r-2][c-2])
            tmp.append(board[r-1][c])
            tmp.append(board[r-1][c-1])
            tmp.append(board[r-1][c-2])
        t=[]
        for item in tmp:
            if item!='.':
                t.append(item)
        return t
    #get column from element row and c number
    def getcol(self,r,c,board):
        t=[]
        for row in range(0,len(board)):
            if row!=r:
                if board[row][c]!='.':
                    t.append(board[row][c])
        return t
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #print(board)
        #perrow
        #check each filled element
        #check its column
        #check its square
        for r in range(0,len(board)):
            for c in range(0,len(board[0])):
                if board[r][c]!='.':
                    rrow=board[r][:c]+board[r][c+1:]
                    #print(rrow)
                    column=self.getcol(r,c,board)
                    square=self.getsquare(r,c,board)
                    comb=column+square+rrow
                    if board[r][c] in comb:
                        return False
        return True
