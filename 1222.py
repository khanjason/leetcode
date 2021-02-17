class Solution:
    def traverse(self,li,board):
        
        for s in li:
            if board[s[0]][s[1]]!='.':
                return s
       
        return '.'
    
    
        
    
    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        count=0
        board=[]
        ans=[]
        for t in range(0,8):
            tmp=[]
            for x in range(0,8):
                tmp.append('.')
            board.append(tmp)
        for coords in queens:
            board[coords[0]][coords[1]]='Q'
        board[king[0]][king[1]]='K'
        
        x=king[0]
        y=king[1]
        #traverse to right
        right=[]
        for t in range(y+1,8):
            right.append([x,t])
        
        
        sq=self.traverse(right,board)
        if sq!='.':
            ans.append(sq)
        #traverse left
        
        
        left=[]
        for t in range(0,y):
            left.append([x,t])
        left=left[::-1]
        sq=self.traverse(left,board)
        if sq!='.':
            ans.append(sq)
        #traverse up
        up=[]
        for i in range(0,x):
            up.append([i,y])
        up=up[::-1]
        sq=self.traverse(up,board)
        if sq!='.':
            ans.append(sq)
        #traverse down
        down=[]
        for d in range(x+1,8):
            down.append([d,y])
        sq=self.traverse(down,board)
        if sq!='.':
            ans.append(sq)
        
        #diagonally upper left
        upleft=[]
        c=1
        for t in range(x-1,-1,-1):
            if (y-c==-1):
                break
            upleft.append([t,y-c])
            c=c+1
        sq=self.traverse(upleft,board)
        if sq!='.':
            ans.append(sq)
        
        #diagonal bottom right
        bottomright=[]
        c=1
        for t in range(x+1,8):
            if (y+c==8):
                break
            bottomright.append([t,y+c])
            c=c+1
        
        sq=self.traverse(bottomright,board)
        if sq!='.':
            ans.append(sq)
        #diagonally upper right
        upright=[]
        c=1
        for t in range(x+1,8):
            if y-c==-1:
                break
            upright.append([t,y-c])
            c=c+1
        
        sq=self.traverse(upright,board)
        if sq!='.':
            ans.append(sq)
        #diagonally bottom left
        bottomleft=[]
        c=1
        for t in range(x-1,-1,-1):
            if y+c==8:
                break
            bottomleft.append([t,y+c])
            c+=1
        sq=self.traverse(bottomleft,board)
        
        if sq!='.':
            ans.append(sq)
        return ans
        
