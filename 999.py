class Solution:
    
    def traverse(self,li):
        for square in li:
            if square!='.':
                return square
        return '.'
    #traverse a direction 
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x=0
        y=0
        count=0
        found=False
        for row in range(0,8):
            for col in range(0,8):
                if board[row][col]=='R':
                    x=row
                    y=col
                    found=True
                    break
            if found:
                break
        
        #traverse to right
        right=board[x][y+1:]
        if self.traverse(right)=='p':
            count=count+1
        #traverse left
        left=board[x][:y]
        left=left[::-1]
        if self.traverse(left)=='p':
            count=count+1
        #traverse up
        up=[]
        for i in range(0,x):
            up.append(board[i][y])
        up=up[::-1]
        if self.traverse(up)=='p':
            count=count+1
        #traverse down
        down=[]
        for d in range(x+1,8):
            down.append(board[d][y])
        if self.traverse(down)=='p':
            count=count+1
        return count
